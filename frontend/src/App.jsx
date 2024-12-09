
import { Outlet } from "react-router-dom"
// import Home from "./components/Home"
import Navbar from "./components/Navbar"

function App() {

  return (
  <div className="bg-gradient-to-b from-custom-blue to-custom-purple min-h-screen font-arimo">
    <Navbar/>
    <Outlet/>
  </div>
  )
}

export default App
