export default function StatsCard({ title, value, icon }) {
  return (
    <div style={styles.card}>
      <div>
        <h4 style={styles.title}>{title}</h4>
        <h2 style={styles.value}>{value}</h2>
      </div>
      <div style={styles.icon}>{icon}</div>
    </div>
  );
}

const styles = {
  card: {
    flex: 1,
    background: " #2563eb", // SAME AS SIDEBAR
    color: "#ffffff",
    padding: "26px",
    borderRadius: "16px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    boxShadow: "0 10px 25px rgba(2,6,23,0.45)",
    transition: "transform 0.2s ease",
  },

  title: {
    fontSize: "15px",
    fontWeight: "500",
    opacity: 0.9,
    marginBottom: "10px",
  },

  value: {
    fontSize: "34px",
    fontWeight: "700",
  },

  icon: {
    fontSize: "36px",
    opacity: 0.9,
  },
};
