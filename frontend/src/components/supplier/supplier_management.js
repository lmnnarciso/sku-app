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

export default function SupplierManagement(props) {
  const classes = useStyles();

  const [values, setValues] = React.useState({
    email: '',
    name: '',
    address: '',
  });

  const {id} = useParams();
  
  const submitForm = () => {
    console.log(values)
    axios.post(`${API_URL}/supplier/add/`, values)
    .then(function (response) {
      props.history.push(`/supplier_list/${response.data.id}`)
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  const editForm = () => {
    axios.patch(`${API_URL}/supplier/detail/${id}/`, values)
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
      axios.get(`${API_URL}/supplier/detail/${id}/`)
      .then(function (response) {
        // console.log(response.data.name)
        setValues(response.data)
      })
      .catch(function (error) {
        props.history.push('/supplier_list')
      });
    }
  }, [])

  const handleChange = name => event => {
    setValues({ ...values, [name]: event.target.value });
  };
  

  return (
    
    <>
    <Typography component="div">
        <Box fontSize="h6.fontSize" m={1}>Add Supplier</Box>
    </Typography>
    <form className={classes.container} noValidate autoComplete="off">
      
      <TextField
        id="standard-full-width"
        label="Email"
        style={{ margin: 8 }}
        placeholder="Supplier Email"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.email}
        onChange={ handleChange('email')}
        InputLabelProps={{
          shrink: true,
        }}
      />
      <TextField
        id="standard-full-width"
        label="Name"
        style={{ margin: 8 }}
        placeholder="Supplier Name"
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
        label="Address"
        style={{ margin: 8 }}
        placeholder="Supplier Address"
        // helperText="Full width!"\
        fullWidth
        margin="normal"
        value={values.address}
        onChange={ handleChange('address')}
        InputLabelProps={{
          shrink: true,
        }}
      />
      <Button variant="contained" color="primary" className={classes.button} onClick={() => id ? editForm() : submitForm() }>
        {id ? 'Edit' : 'Submit'} 
    </Button>
    <Button variant="contained" color="secondary" className={classes.button}>
        <Link to="/supplier_list">Back</Link>
    </Button>
    </form>
    
    
		</>
  );
}
