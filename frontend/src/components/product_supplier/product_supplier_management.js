import React, { useEffect } from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';

import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Select from '@material-ui/core/Select';

import {Link, useParams} from 'react-router-dom';
import axios from 'axios';


import InputLabel from '@material-ui/core/InputLabel';
import DateFnsUtils from '@date-io/date-fns';
import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker,
} from '@material-ui/pickers';

const useStyles = makeStyles(theme => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 200,
  },
  dense: {
    marginTop: 19,
  },
  menu: {
    width: 200,
  },
}));

const API_URL = 'http://127.0.0.1:8000/api'

export default function ProductSupplierManagement(props) {
  const classes = useStyles();

  const [values, setValues] = React.useState({
    product_id: null,
    supplier_id: null,
    date_to_supply: '',
    quantity_supply: 1,
    price: 1,
  });

  const [product, setProduct] = React.useState([])
  const [supplier, setSupplier] = React.useState([])

  const [selectedDate, setSelectedDate] = React.useState(new Date('2014-08-18T21:11:54'));

  const handleDateChange = date => {
    // setSelectedDate(date);
    setValues({...values, date_to_supply: date})
  };

  const {id} = useParams();

  let fetchProduct = () => {
    axios.get(`${API_URL}/product/list/`)
      .then(function (response) {
        // handle success
        console.log(response)
        setProduct([...response.data])
      })
      .catch(function (error) {
        // handle error
        console.log(error);
        props.history.push('/product_supplier_list')
      })
      .finally(function () {
        // always executed
      });
  }

  let fetchSupplier = () => {
    axios.get(`${API_URL}/supplier/list/`)
      .then(function (response) {
        // handle success
        console.log(response)
        setSupplier([...response.data])
      })
      .catch(function (error) {
        // handle error
        console.log(error);
        props.history.push('/product_supplier_list')
      })
      .finally(function () {
        // always executed
      });
  }

  const submitForm = () => {
    console.log(values)
    axios.post(`${API_URL}/product/product_supplier/add/`, values)
    .then(function (response) {
      props.history.push(`/product_supplier_list/${response.data.id}`)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const editForm = () => {
    axios.patch(`${API_URL}/product/product_supplier/detail/${id}/`, values)
    .then(function (response) {
      console.log("successfully edited")
      // props.history.push(`/product_category_list/${response.data.id}`)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  useEffect(() => {
    if(id){
      axios.get(`${API_URL}/product/product_supplier/detail/${id}/`)
      .then(function (response) {
        // console.log(response.data.name)
        setValues(response.data)
      })
      .catch(function (error) {
        props.history.push('/product_supplier_list')
      });
    }
    
    fetchProduct();
    fetchSupplier();
  }, [])

  const handleChange = name => event => {
    setValues({ ...values, [name]: event.target.value });
  };
  

  return (
    
    <>
    <Typography component="div">
        <Box fontSize="h6.fontSize" m={1}>Add Product Supplier</Box>
    </Typography>
    <form className={classes.container} noValidate autoComplete="off">
        
        <InputLabel htmlFor="product_id">Product</InputLabel>
        <Select
              label="Product"
              fullWidth
              value={values.product_id}
              onChange={handleChange('product_id')}
              inputProps={{
                name: 'product',
                id: 'product_id',
              }}
            >
          {product.map(item => {
            return <MenuItem value={item.id}>{item.name}</MenuItem>
          })}
        </Select>
        
        <InputLabel htmlFor="supplier_id">Supplier</InputLabel>
        <Select
              label="Supplier"
              fullWidth
              value={values.supplier_id}
              onChange={handleChange('supplier_id')}
              inputProps={{
                name: 'supplier',
                id: 'supplier_id',
              }}
            >
          {supplier.map(item => {
            return <MenuItem value={item.id}>{item.name}</MenuItem>
          })}
        </Select>

        
        <MuiPickersUtilsProvider utils={DateFnsUtils}>
          <KeyboardDatePicker
            fullWidth
            margin="normal"
            id="date-picker-dialog"
            label="Date picker dialog"
            format="MM/dd/yyyy"
            value={selectedDate}
            onChange={handleDateChange}
            KeyboardButtonProps={{
              'aria-label': 'change date',
            }}
          />
        </MuiPickersUtilsProvider>
        
      {/* <TextField
        id="standard-full-width"
        label="Date"
        style={{ margin: 8 }}
        placeholder="Date to supply"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.description}
        onChange={ handleChange('description')}
        InputLabelProps={{
          shrink: true,
        }}
      /> */}

      <TextField
        id="standard-full-width"
        label="Unit Price"
        style={{ margin: 8 }}
        placeholder="Product unit price"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.unit_price}
        onChange={ handleChange('unit_price')}
        InputLabelProps={{
          shrink: true,
        }}
      />
      <TextField
        id="standard-full-width"
        label="Quantity"
        style={{ margin: 8 }}
        placeholder="Product Quantity"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.quantity}
        onChange={ handleChange('quantity')}
        InputLabelProps={{
          shrink: true,
        }}
      />
      <Button variant="contained" color="primary" className={classes.button} onClick={() => id ? editForm() : submitForm() }>
        {id ? 'Edit' : 'Submit'} 
    </Button>
    <Button variant="contained" color="secondary" className={classes.button}>
        <Link to="/product_supplier_list">Back</Link>
    </Button>
    </form>
    
    
		</>
  );
}
