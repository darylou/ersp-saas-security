import { useState } from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import './App.css'
import Home from './pages/Home.js'
import Login from './pages/Login.js'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Login />}/>
            <Route path="pastes" element={<Home />}/>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
