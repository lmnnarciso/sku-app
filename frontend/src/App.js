
import React, { Component } from 'react';
// import './App.css';
import { BrowserRouter, Switch } from 'react-router-dom';
// import Home from './components/home';
import Dashboard from './components/dashboard';
import SignIn from './components/login';
import PrivateRoute from './routes/PrivateRoute';
import PublicRoute from './routes/PublicRoute';

class App extends Component {

  render() {
    return (
      <BrowserRouter>
        <Switch>
          {/* <PublicRoute restricted={false} component={Home} path="/" exact /> */}
          <PublicRoute restricted={true} component={SignIn} path="/" exact />
          <PrivateRoute component={Dashboard} path="/dashboard" exact />
        </Switch>
      </BrowserRouter>
    );
  }
}


export default App;