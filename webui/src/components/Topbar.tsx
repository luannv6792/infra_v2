import { useTheme } from "../theme/ThemeContext";

export default function Topbar() {
  const { theme, toggle } = useTheme();

  return (
    <div style={{
      padding: "12px 24px",
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      borderBottom: "1px solid var(--muted)"
    }}>
      <strong>Deploy Monitor</strong>

      <button onClick={toggle}>
        {theme === "light" ? "🌙 Dark" : "☀️ Light"}
      </button>
    </div>
  );
}
