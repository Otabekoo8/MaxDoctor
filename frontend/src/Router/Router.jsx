import * as React from "react";
// import * as ReactDOM from "react-dom/client";
import { createBrowserRouter } from "react-router-dom";
import Login from "../Login/Login";
import Home from "../Home/Home";







const router = createBrowserRouter([
    {
        path: "/",
        element: <Login />
    },
    {
        path: "/kirish",
        element:<Home/>
    }
  

]);

export default router;