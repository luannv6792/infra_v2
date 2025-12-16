import { useEffect, useState } from "react";
import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";

export default function Reports() {
  const { user } = useAuth();
  const [monthData, setMonthData] = useState([]);
  const [yearData, setYearData] = useState([]);

  useEffect(() => {
    if (!user || user.role !== "admin") return;

    api("/api/reports/monthly?month=2025-09-01", user.token).then(setMonthData);
    api("/api/reports/yearly?year=2025", user.token).then(setYearData);
  }, [user]);

  if (!user || user.role !== "admin") {
    return <p>Access denied</p>;
  }

  return (
    <div style={{ padding: 24 }}>
      <h2>Monthly Report</h2>
      <pre>{JSON.stringify(monthData, null, 2)}</pre>

      <h2 style={{ marginTop: 24 }}>Yearly Report</h2>
      <pre>{JSON.stringify(yearData, null, 2)}</pre>
    </div>
  );
}
