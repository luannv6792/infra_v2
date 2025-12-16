import { useAuth } from "../auth/AuthContext";
import { api } from "../api/client";
import { useEffect, useState } from "react";

export default function Reports() {
  const { user } = useAuth();
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    api<any[]>("/api/reports/monthly?month=2025-09-01", user?.token)
      .then(setData);
  }, []);

  return (
    <div>
      <h2>Monthly Report</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
