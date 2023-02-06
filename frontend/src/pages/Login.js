import React, { useState } from "react"
import { Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/tabs'
import axios from 'axios'

function Login() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    
    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    function onLogin() {
        // Do something here
        // Show message if there's a login issue

    }

    const onRegister = async (e) => {
        e.preventDefault()
        const post = { 
            'user': username,  
            'passw': password 
        }
        try {
          const res = await axios.post('http://127.0.0.1:3030/auth/create', post)
          console.log(res.data)
          console.log("success")
        } catch (e) {
          alert(e)
        }
      }
    
    return (
        <div className='login_container'>
            <h1>GooBox</h1>

            <Tabs variant='unstyled'>
            <TabList className="tab_list">
                <Tab className='tab' _selected={{ color: 'black', textDecoration: 'underline' }}>Login</Tab>
                <Tab className='tab' _selected={{ color: 'black', textDecoration: 'underline' }}>Create Account</Tab>
            </TabList>

            <TabPanels>
                <TabPanel>
                <div className="login_container">
                <p>Username</p>
                <input id='username' onChange={handleUsernameChange}/>
                <p>Password</p>
                <input id='password' onChange={handlePasswordChange}/>
                <br />
                <button className='btn' onClick={onLogin}>Submit</button>
                </div>
                </TabPanel>

                <TabPanel>
                <div className="login_container">
                <p>Username</p>
                <input id='username' onChange={handleUsernameChange}/>
                <p>Password</p>
                <input id='password' onChange={handlePasswordChange}/>
                <br />
                <button className='btn' onClick={onRegister}>Submit</button>
                </div>
                </TabPanel>
            </TabPanels>
            </Tabs>
        </div>
    )
}

export default Login