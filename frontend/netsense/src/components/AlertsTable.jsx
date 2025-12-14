export default function AlertsTable({ alerts }) {
  if (!alerts.length) return null;

  return (
    <div style={styles.wrapper}>
      <h3>Detection Results</h3>

      <table style={styles.table}>
        <thead>
          <tr>
            <th>#</th>
            <th>Score</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((a, i) => (
            <tr key={i}>
              <td>{i + 1}</td>
              <td>{a.score.toFixed(5)}</td>
              <td
                style={{
                  color: a.is_anomaly ? "#dc2626" : "#16a34a",
                  fontWeight: "bold",
                }}
              >
                {a.is_anomaly ? "ANOMALY" : "NORMAL"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const styles = {
  wrapper: {
    background: "#ffffff",
    padding: "25px",
    borderRadius: "10px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "15px",
  },
};
