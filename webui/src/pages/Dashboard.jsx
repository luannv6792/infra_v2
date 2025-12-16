import { useEffect, useState } from "react";
import DeployTable from "../components/DeployTable";
import DeployChart from "../components/DeployChart";
import AlertBanner from "../components/AlertBanner";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";

export default function Dashboard() {
  const { user } = useAuth();

  const [data, setData] = useState([]);
  const [alert, setAlert] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!user) return;

    api("/api/deployments/today", user.token)
      .then(setData)
      .catch(() => setError("Failed to fetch deployments"));

    // Alert today (admin only)
    if (user.role === "admin") {
      api("/api/alerts/today", user.token).then(setAlert);
    }
  }, [user]);

  if (!user) return null;
  if (error) return <p>Error: {error}</p>;

  return (
    <div style={{ padding: 24 }}>
      <AlertBanner alert={alert} />

      <h2>Deployments Today</h2>
      <DeployChart data={data} />

      <h3>Details</h3>
      <DeployTable data={data} />
    </div>
  );
}
