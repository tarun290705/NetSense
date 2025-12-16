import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./App.css";
import { AuthProvider } from "./context/AuthContext";
import { APIProvider } from "./context/APIContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <AuthProvider>
      <APIProvider>
        <App />
      </APIProvider>
    </AuthProvider>
  </BrowserRouter>
);
