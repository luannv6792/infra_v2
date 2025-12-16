import { useAuth } from "./auth/AuthContext";
import Dashboard from "./pages/Dashboard";
import Topbar from "./components/Topbar";
import Login from "./pages/Login";

export default function App() {
  const { user } = useAuth();

  // Chưa login → show Login page
  if (!user) {
    return <Login />;
  }

  // Đã login
  return (
    <>
      <Topbar />
      <Dashboard />
    </>
  );
}
