import React from 'react'
import Home from './components/Home'
import { Routes, Route } from 'react-router-dom'
import Login from './components/Login'
import Register from './components/Register'
import Dashboard from './components/Dashboard'
import PrivateRoute from './middleware/PrivateRoute'
import GuestRoute from './middleware/GuestRoute'


const App = () => {
  return (
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path='/login' element={<GuestRoute><Login /></GuestRoute>} />
      <Route path='/register' element={<GuestRoute><Register /></GuestRoute>} />
      <Route path='/dashboard' element={<PrivateRoute><Dashboard /></PrivateRoute>} />
    </Routes>
  )
}

export default App