
import React, { Component } from 'react';
// import './App.css';
import { BrowserRouter, Switch } from 'react-router-dom';

import Dashboard from './components/dashboard';
import SignIn from './components/login';
import PrivateRoute from './routes/PrivateRoute';
import PublicRoute from './routes/PublicRoute';


import ProductCategoryList from './components/product_category/product_category_list';
import ProductCategoryManagement from './components/product_category/product_category_management';

class App extends Component {

  render() {
    return (
      <BrowserRouter>
        <Switch>
          {/* <PublicRoute restricted={false} component={Home} path="/" exact /> */}
          <PublicRoute restricted={true} component={SignIn} path="/" exact />
          <PrivateRoute component={Dashboard} path="/dashboard" exact />
          <PrivateRoute component={ProductCategoryList} path="/product_category_list" exact />
          <PrivateRoute component={ProductCategoryManagement} path="/product_category_list/add" exact />
        </Switch>
      </BrowserRouter>
    );
  }
}


export default App;