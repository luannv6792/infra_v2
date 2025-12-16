import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Entry point của WebUI
// KHÔNG gọi API ở đây
// Chỉ mount React App
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
