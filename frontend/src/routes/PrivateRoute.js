import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { isLogin } from '../utils/utility';

import { AppBar } from '@material-ui/core';

import PersistentDrawer from './navigation_drawer';
import Container from '@material-ui/core/Container';

const PrivateRoute = ({component: Component, ...rest}) => {
    return (
        <Route {...rest} render={props => (
            isLogin() ?
                <>
                    <AppBar>
                        Trial
                    </AppBar>
                      <PersistentDrawer>
                        <Container maxWidth="lg">
                          <Component {...props} />
                        </Container>
                      </PersistentDrawer>
                </>
            : <Redirect to="/" />
        )} />
    );
};

export default PrivateRoute;