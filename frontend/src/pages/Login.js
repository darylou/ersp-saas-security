import React, { useState } from "react"
import { Tabs, TabList, TabPanels, Tab, TabPanel } from '@chakra-ui/tabs'
import axios from 'axios'
import { useNavigate } from "react-router-dom"

function Login() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate();
    
    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handlePasswordChange = (e) => {
        setPassword(e.target.value)
    }

    function onLogin() {
        axios.get(`http://127.0.0.1:3030/auth/auth/${username}/${password}`).then((res) => {
            console.log("Success");
            navigate("/pastes",{state:{authenticated:true}})
        }).catch((err) => {
            console.log("bad login")
        })
    }

    const onRegister = async (e) => {
        e.preventDefault()
        const post = { 
            'user': username,  
            'passw': password 
        }
        try {
            const res = await axios.post(`http://127.0.0.1:3030/auth/create/${username}/${password}`, post)
            console.log(res.data)
            console.log("success")
            navigate("/pastes",{state:{authenticated:true}})
        } catch (e) {
            console.log("fail")
            alert(e)
        }
      }
    
    return (
        <div className='login_container' style={{overflow: "clip"}}>
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

            <br/>
            <p>Note: please do not input any sensitive or personal information into this application. All accounts and data will be periodically destroyed to ensure safety.</p>
        </div>
    )
}

export default Login