import { useEffect, useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";
import Layout from "../components/Layout";
import Card from "../components/Card";
import DeployChart from "../components/DeployChart";
import DeployTable from "../components/DeployTable";
import AlertBanner from "../components/AlertBanner";

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

    if (user.role === "admin") {
      api("/api/alerts/today", user.token).then(setAlert);
    }
  }, [user]);

  if (!user) return null;
  if (error) return <p>{error}</p>;

  return (
    <Layout>
      <AlertBanner alert={alert} />

      <Card title="Deployments Today">
        <DeployChart data={data} />
      </Card>

      <Card title="Details">
        <DeployTable data={data} />
      </Card>
    </Layout>
  );
}
