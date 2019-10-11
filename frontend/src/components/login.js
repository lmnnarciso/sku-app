import React from 'react';
import { login } from '../utils/utility.js';

// const SignIn = (props) => {

//     const handleLogin = () => {
//         login();
//         props.history.push('/dashboard');
//     }

//     return (
//         <div>
//             <h1>Sign in</h1>

//             <button onClick={() => handleLogin()}>Click here to log in</button>
//         </div>
//     );
// };

// export default SignIn;

const Login = (props) => {

  // const response = await fetch('http://127.0.0.1:8000/api/product/list/');
  // const myJson = await response.json();
  // console.log('dead');
  const handleLogin = () => {
      login();
      props.history.push('/dashboard');
  }

  return (
    <div className="App " >
    <div className="w-full max-w-md h-screen flex items-center mx-auto" >
      <form action="" className="w-full bg-white shadow-md rounded px-8 py-8 pt-8">
        <div className="px-4 pb-4">
          <label htmlFor="email" className="text-sm block font-bold  pb-2">EMAIL ADDRESS</label>
          <input type="email" name="email" id="" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline border-blue-300 " placeholder="Johnbull@example.com"/>
        </div>
        <div  className="px-4 pb-4">
          <label htmlFor="password" className="text-sm block font-bold pb-2">PASSWORD</label>
          <input type="password" name="email" id="" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline border-blue-300" placeholder="Enter your password"/>
        </div>
        <div>
          <button onClick={() => handleLogin()} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">Sign In</button>
        </div>
      </form>
    </div>
  </div>
  );
}

export default Login;
