import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Home } from "./Home";
import { Khoa } from "./Khoa";
import { SinhVien } from "./SinhVien";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <BrowserRouter>
      <div className="App Test">
        <h3>Demo React Router Dom</h3>
        <nav className='navbar navbar-expand-sm bg-light navbar-dark'>
          <ul className='navbar-nav'>
            <li className='nav-item m-1'>
                <NavLink className="btn btn-ligh btn-outline-primary" to="/home">Home</NavLink>
            </li>
            <li className='nav-item m-1'>
                <NavLink className="btn btn-ligh btn-outline-primary" to="/khoa">Khoa</NavLink>
            </li>
            <li className='nav-item m-1'>
                <NavLink className="btn btn-ligh btn-outline-primary" to="/sinhvien">SinhVien</NavLink>
            </li>
          </ul> 
        </nav>
        <Routes>
            <Route path="/home" element={<Home />} />
            <Route path="/khoa" element={<Khoa />} />
            <Route path="/sinhvien" element={<SinhVien />} />
        </Routes>
      </div>
    </BrowserRouter>
    </>
  )
}

export default App
