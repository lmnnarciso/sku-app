import React from 'react';
import {logout, isLogin} from '../utils/utility'
import axios from 'axios'
import { Link } from 'react-router-dom';


class Dashboard  extends React.Component{
    constructor(props){
        super(props)

        this.state = {
            isLogin: isLogin()
        }
    }

    fetchData = () => {
        axios.get('http://127.0.0.1:8000/api/product/list/')
        .then((res) => {
            console.log(res)
        })
        .catch((err) => {
            console.log(err)
        })
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
    
    componentDidMount(){
        this.fetchData()
    }
};

export default Dashboard;