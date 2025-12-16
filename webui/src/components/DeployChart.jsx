import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function DeployChart({ data }) {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <XAxis dataKey="application" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="total" />
      </BarChart>
    </ResponsiveContainer>
  );
}
