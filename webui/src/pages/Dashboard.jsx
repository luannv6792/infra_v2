import { useEffect, useState } from "react";
import DeployTable from "../components/DeployTable";
import DeployChart from "../components/DeployChart";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";

export default function Dashboard() {
  const { user } = useAuth();

  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!user) return;

    api("/api/deployments/today", user.token)
      .then(setData)
      .catch(err => {
        console.error(err);
        setError("Failed to fetch deployments");
      });
  }, [user]);

  if (!user) return <p>Please login</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div style={{ padding: 24 }}>
      <h2>Deployments Today</h2>

      <DeployChart data={data} />

      <h3>Details</h3>
      <DeployTable data={data} />
    </div>
  );
}
