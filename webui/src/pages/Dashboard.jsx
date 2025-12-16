import { useEffect, useState } from "react";
import DeployTable from "../components/DeployTable";
import DeployChart from "../components/DeployChart";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";

type DeploymentToday = {
  application: string;
  environment: string;
  total: number;
};

export default function Dashboard() {
  const { user } = useAuth();

  const [data, setData] = useState<DeploymentToday[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user) return;

    api<DeploymentToday[]>("/api/deployments/today", user.token)
      .then(setData)
      .catch(err => {
        console.error(err);
        setError("Failed to fetch deployments");
      });
  }, [user]);

  if (error) return <p>Error: {error}</p>;
  if (!user) return <p>Please login</p>;

  return (
    <div style={{ padding: 24 }}>
      <h2>Deployments Today</h2>

      <DeployChart data={data} />

      <h3>Details</h3>
      <DeployTable data={data} />
    </div>
  );
}
