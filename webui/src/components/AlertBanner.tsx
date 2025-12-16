export default function AlertBanner({ alert }) {
  if (!alert?.has_failed) return null;
  return (
    <div style={{ background: "#fee2e2", padding: 12, borderRadius: 8 }}>
      🚨 <b>{alert.failed_count} deploy FAILED hôm nay</b> – {alert.applications.join(", ")}
    </div>
  );
}
