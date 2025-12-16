import { useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";

export default function Login() {
  const { login } = useAuth();
  const [username, setU] = useState("admin");
  const [password, setP] = useState("admin");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const submit = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await api("/api/auth/login", null, {
        method: "POST",
        body: JSON.stringify({ username, password }),
      });
      login({ token: res.access_token, role: res.role });
    } catch (e) {
      setError("Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 40, maxWidth: 360, margin: "80px auto" }}>
      <h2>Login</h2>

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setU(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setP(e.target.value)}
      />

      <button onClick={submit} disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
