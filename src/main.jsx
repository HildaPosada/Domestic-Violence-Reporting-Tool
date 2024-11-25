import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Resources from './pages/Resources.jsx'
import SafetyTips from './pages/SafetyTips.jsx'

const router = createBrowserRouter([
  { path: "/", element: <App/> },
  { path: "/resources", element: <Resources/> },
  { path: "/safetyTips", element: <SafetyTips/> },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
   <RouterProvider router={router}/>
  </StrictMode>,
)
