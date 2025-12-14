export default function TrafficGraph() {
  return (
    <div style={styles.card}>
      <h3 style={styles.title}>Traffic Trend</h3>
      <p style={styles.subtitle}>
        Graph visualization can be added here
      </p>
    </div>
  );
}

const styles = {
  card: {
    background: " #2563eb", // SAME AS SIDEBAR
    color: "#ffffff",
    padding: "28px",
    borderRadius: "18px",
    boxShadow: "0 12px 28px rgba(2,6,23,0.45)",
    marginTop: "40px",
  },

  title: {
    fontSize: "20px",
    fontWeight: "600",
    marginBottom: "12px",
  },

  subtitle: {
    fontSize: "15px",
    opacity: 0.85,
  },
};
