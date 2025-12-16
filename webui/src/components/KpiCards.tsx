export default function KpiCards({ data }) {
  const total = data.reduce((s, r) => s + r.total, 0);

  return (
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16 }}>
      <Card title="Total Deploy" value={total} />
      <Card title="Applications" value={new Set(data.map(d => d.application)).size} />
      <Card title="Environments" value={new Set(data.map(d => d.environment)).size} />
      <Card title="Status" value="OK" />
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div style={{
      background: "var(--card)",
      padding: 20,
      borderRadius: 12,
      boxShadow: "0 4px 12px rgba(0,0,0,.05)"
    }}>
      <div style={{ color: "var(--muted)", fontSize: 12 }}>{title}</div>
      <div style={{ fontSize: 28, fontWeight: 600 }}>{value}</div>
    </div>
  );
}
