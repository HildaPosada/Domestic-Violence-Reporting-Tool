import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Resources from "./pages/Resources.jsx";
import SafetyTips from "./pages/SafetyTips.jsx";
import FollowUpReports from "./components/FollowUpReports";
import Registration from "./agency-ui/Registration.jsx";
import Home from "./components/Home.jsx";


const router = createBrowserRouter([
  {
    path: "/", 
    element: <App />, 
    children: [
      { index: true, element: <Home /> },
      { path: "resources", element: <Resources /> },
      { path: "safetyTips", element: <SafetyTips /> },
      { path: "follow-up-reports", element: <FollowUpReports /> }, // Add this route
      
    ]
  },
  { path: "/agency-registration", element: <Registration /> }

]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
