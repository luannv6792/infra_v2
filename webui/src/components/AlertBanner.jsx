export default function AlertBanner({ alert }) {
  if (!alert || !alert.has_failed) return null;

  return (
    <div
      style={{
        background: "#fee2e2",
        color: "#991b1b",
        padding: 16,
        borderRadius: 12,
        marginBottom: 16,
        border: "1px solid #fecaca",
      }}
    >
      🚨 <strong>{alert.failed_count} deploy FAILED hôm nay</strong>
      <div style={{ marginTop: 4 }}>
        Ứng dụng ảnh hưởng: {alert.applications.join(", ")}
      </div>
    </div>
  );
}
