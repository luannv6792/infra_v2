import { useEffect, useState } from "react";
import { fetchTodayDeployments } from "../api/deploymentApi";
import DeployTable from "../components/DeployTable";
import DeployChart from "../components/DeployChart";

export default function Dashboard() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTodayDeployments()
      .then(setData)
      .catch(err => setError(err.message));
  }, []);

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
