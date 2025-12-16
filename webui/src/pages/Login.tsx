import { useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";

export default function Login() {
  const { login } = useAuth();
  const [username, setU] = useState("admin");
  const [password, setP] = useState("admin");

  const submit = async () => {
    const res = await api<{ access_token: string; role: any }>(
      "/api/auth/login",
      undefined,
      {
        method: "POST",
        body: JSON.stringify({ username, password }),
      }
    );
    login({ token: res.access_token, role: res.role });
  };

  return (
    <div style={{ padding: 40, maxWidth: 360, margin: "80px auto" }}>
      <h2>Login</h2>
      <input value={username} onChange={e => setU(e.target.value)} />
      <input type="password" value={password} onChange={e => setP(e.target.value)} />
      <button onClick={submit}>Login</button>
    </div>
  );
}
