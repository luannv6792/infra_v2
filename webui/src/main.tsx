import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

const App = () => {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    fetch("/api/hello")
      .then(res => res.json())
      .then(data => setMsg(data.message))
      .catch(() => setMsg("Backend not reachable"));
  }, []);

  return <h1>{msg}</h1>;
};

createRoot(document.getElementById("root")!).render(<App />);
