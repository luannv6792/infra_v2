import { useAuth } from "../auth/AuthContext";
import { useTheme } from "../theme/ThemeContext";

export default function Topbar() {
  const { user, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();

  if (!user) return null;

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "12px 24px",
        borderBottom: "1px solid #e5e7eb",
      }}
    >
      {/* Left */}
      <strong>Deploy Monitor</strong>

      {/* Right */}
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        {/* 🌗 Theme toggle */}
        <button onClick={toggleTheme}>
          {theme === "dark" ? "🌙 Dark" : "☀️ Light"}
        </button>

        {/* Role */}
        <span>
          Role: <b>{user.role}</b>
        </span>

        {/* Logout */}
        <button onClick={logout}>Logout</button>
      </div>
    </div>
  );
}
