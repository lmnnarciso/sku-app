import React, { useEffect } from 'react';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';

import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

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

const currencies = [
  {
    value: 'USD',
    label: '$',
  },
  {
    value: 'EUR',
    label: '€',
  },
  {
    value: 'BTC',
    label: '฿',
  },
  {
    value: 'JPY',
    label: '¥',
  },
];

const API_URL = 'http://127.0.0.1:8000/api'

export default function ProductCategoryManagement(props) {
  const classes = useStyles();

  const [values, setValues] = React.useState({
    name: '',
    description: '',
  });

  const {id} = useParams();
  
  const submitForm = () => {
    console.log(values)
    axios.post(`${API_URL}/product/product_category/add`, values)
    .then(function (response) {
      props.history.push(`/product_category_list/${response.data.id}`)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const editForm = () => {
    axios.patch(`${API_URL}/product/product_category/detail/${id}/`, values)
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
      axios.get(`${API_URL}/product/product_category/detail/${id}/`)
      .then(function (response) {
        // console.log(response.data.name)
        setValues(response.data)
      })
      .catch(function (error) {
        props.history.push('/product_category_list')
      });
    }
  }, [])

  const handleChange = name => event => {
    setValues({ ...values, [name]: event.target.value });
  };
  

  return (
    
    <>
    {
      console.log(values)
    }
    <Typography component="div">
        <Box fontSize="h6.fontSize" m={1}>Add Product Category</Box>
    </Typography>
    <form className={classes.container} noValidate autoComplete="off">
      {/* <TextField
        id="standard-name"
        label="Name"
        fullWidth
        className={classes.textField}
        value={values.name}
        onChange={handleChange('name')}
        margin="normal"
      />
      <TextField
        id="standard-dense"
        label="Dense"
        className={clsx(classes.textField, classes.dense)}
        fullWidth
        margin="dense"
      />
      <TextField
        id="standard-with-placeholder"
        label="With placeholder"
        placeholder="Placeholder"
        className={classes.textField}
        fullWidth
        margin="normal"
      /> */}
      
      <TextField
        id="standard-full-width"
        label="Name"
        style={{ margin: 8 }}
        placeholder="Product Category"
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
        placeholder="Product Category Description"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.description}
        onChange={ handleChange('description')}
        InputLabelProps={{
          shrink: true,
        }}
      />
      <Button variant="contained" color="primary" className={classes.button} onClick={() => id ? editForm() : submitForm() }>
        {id ? 'Edit' : 'Submit'} 
    </Button>
    <Button variant="contained" color="secondary" className={classes.button}>
        <Link to="/product_category_list/">Back</Link>
    </Button>
    </form>
    
    
		</>
  );
}
