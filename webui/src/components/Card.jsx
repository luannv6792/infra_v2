export default function Card({ title, children }) {
  return (
    <div
      style={{
        background: "var(--card)",
        borderRadius: 16,
        padding: 20,
        boxShadow:
          "0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.06)",
        marginBottom: 20,
      }}
    >
      {title && (
        <h3 style={{ marginTop: 0, marginBottom: 12 }}>{title}</h3>
      )}
      {children}
    </div>
  );
}
