import { useAuth } from "../auth/AuthContext";

export default function Topbar() {
  const { user, logout } = useAuth();

  if (!user) return null;

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "12px 24px",
        borderBottom: "1px solid #e5e7eb",
      }}
    >
      <strong>Deploy Monitor</strong>

      <div>
        <span style={{ marginRight: 12 }}>
          Role: <b>{user.role}</b>
        </span>
        <button onClick={logout}>Logout</button>
      </div>
    </div>
  );
}
