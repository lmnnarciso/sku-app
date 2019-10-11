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

export default function ProductManagement(props) {
  const classes = useStyles();

  const [values, setValues] = React.useState({
    product_category_id: null,
    name: '',
    description: '',
    quantity: 1,
    unit_price: 1,
  });

  const [productCategory, setProductCategory] = React.useState([])

  const {id} = useParams();

  let fetchProductCategory = () => {
    axios.get(`${API_URL}/product/product_category/list/`)
      .then(function (response) {
        // handle success
        console.log(response)
        setProductCategory([...response.data])
      })
      .catch(function (error) {
        // handle error
        console.log(error);
        console.log("please add a product category first")
      })
      .finally(function () {
        // always executed
      });
  }
  const submitForm = () => {
    console.log(values)
    axios.post(`${API_URL}/product/add/`, values)
    .then(function (response) {
      props.history.push(`/product_list/${response.data.id}`)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const editForm = () => {
    axios.patch(`${API_URL}/product/detail/${id}/`, values)
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
      axios.get(`${API_URL}/product/detail/${id}/`)
      .then(function (response) {
        // console.log(response.data.name)
        setValues(response.data)
      })
      .catch(function (error) {
        props.history.push('/product_list')
      });
    }
    fetchProductCategory()
  }, [])

  const handleChange = name => event => {
    setValues({ ...values, [name]: event.target.value });
  };
  

  return (
    
    <>
    <Typography component="div">
        <Box fontSize="h6.fontSize" m={1}>Add Product</Box>
    </Typography>
    <form className={classes.container} noValidate autoComplete="off">
        <Select
              fullWidth
              value={values.product_category_id}
              onChange={handleChange('product_category_id')}
              inputProps={{
                name: 'product_category',
                id: 'product_category_id',
              }}
            >
          {productCategory.map(item => {
            return <MenuItem value={item.id}>{item.name}</MenuItem>
          })}
        </Select>

      <TextField
        id="standard-full-width"
        label="Name"
        style={{ margin: 8 }}
        placeholder="Product name"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.name}
        onChange={ handleChange('name')}
        InputLabelProps={{
          shrink: true,
        }}
      />
      <TextField
        id="standard-full-width"
        label="Description"
        style={{ margin: 8 }}
        placeholder="Product Description"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.description}
        onChange={ handleChange('description')}
        InputLabelProps={{
          shrink: true,
        }}
      />
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
        <Link to="/product_list">Back</Link>
    </Button>
    </form>
    
    
		</>
  );
}
