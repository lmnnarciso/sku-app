import React from 'react';
import {logout, isLogin} from '../utils/utility'

import { Link } from 'react-router-dom';


class Dashboard  extends React.Component{
    constructor(props){
        super(props)

        this.state = {
            isLogin: isLogin()
        }
    }
    handleLogout = () => {
        logout();
        this.setState({
            isLogin: false
        })
        this.props.history.push("/")
    }
    render(){
        return (
            <div>
                Dashboard
                {
                    this.state.isLogin ?
                    <button onClick={()=> this.handleLogout()} type="button">Logout</button>
                    : 
                    <Link to="/">Logout</Link>
                }
                
    
            </div>
        );
    }
    
};

export default Dashboard;