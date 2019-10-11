import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import { Icon } from '@material-ui/core';

import {Link} from 'react-router-dom';
import axios from 'axios';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(3),
    overflowX: 'auto',
  },
  table: {
    minWidth: 650,
  },
}));

function createData(id, product_category, name, description, unit_price, quantity) {
  return { id, product_category, name, description, unit_price, quantity };
}

const rows = [
  createData(420, 'category1', 'product1', 'Dummy Product #1(For displaying only)', 124, 1000),
  createData(69, 'category2', 'product2', 'Dummy Product #2(For displaying only)', 143, 1000),
  createData(314, 'category3', 'product3',  'Dummy Product #3(For displaying only)', 72, 1000),
];
const API_URL = 'http://127.0.0.1:8000/api'

export default function SupplierList(props) {
  const classes = useStyles();
  const [data, setData] = useState(rows)

  let fetchList = () => {
    axios.get(`${API_URL}/product/list/`)
      .then(function (response) {
        // handle success
        console.log(response)
        setData([...rows, ...response.data])
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .finally(function () {
        // always executed
      });
  }
  useEffect(() => {
    axios.get(`${API_URL}/product/list/`)
      .then(function (response) {
        // handle success
        console.log(response)
        setData([...rows, ...response.data])
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .finally(function () {
        // always executed
      });
  }, []);

  let deleteItem = (id) => {
    axios.delete(`${API_URL}/product/detail/${id}/`)
    .then(function (response) {
      console.log("successfully deleted")
      fetchList()
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  return (
      <>
    <Button variant="contained" color="primary" className={classes.button}>
        <Link to="/product_list/add/">Add Product</Link>
    </Button>
    <Paper className={classes.root}>
    <Typography component="div">
        <Box fontSize="h6.fontSize" m={1}>Product List</Box>
    </Typography>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <TableCell className="hidden-xs">ID</TableCell>
            <TableCell align="right">Product Category</TableCell>
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Description</TableCell>
            <TableCell align="right">Unit Price</TableCell>
            <TableCell align="right">Quantity</TableCell>
            <TableCell align="right">Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map(row => (
              <TableRow key={row.name}>
                <Link to={`/product_list/${row.id}`}>
                    <TableCell component="th" scope="row">
                      {row.id}
                    </TableCell>
                </Link>
                <TableCell align="right">{row.product_category}</TableCell>
                <TableCell align="right">{row.name}</TableCell>
                <TableCell align="right">{row.description}</TableCell>
                <TableCell align="right">{row.unit_price}</TableCell>
                <TableCell align="right">{row.quantity}</TableCell>
                <TableCell align="right"><DeleteForeverIcon onClick={() => deleteItem(row.id)}/></TableCell>
              </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
    </>
  );
}
