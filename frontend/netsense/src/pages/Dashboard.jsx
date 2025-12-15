import { useState } from "react";
import { NavLink } from "react-router-dom";
import UploadDataset from "../components/UploadDataset";
import AlertsTable from "../components/AlertsTable";
import TrafficGraph from "../components/TrafficGraph";
import StatsCard from "../components/statsCard";

export default function Dashboard() {
  const [results, setResults] = useState([]);

  const total = results.length;
  const anomalies = results.filter((r) => r.is_anomaly).length;

  return (
    <div style={styles.page}>
      {/* HERO SECTION */}
      <div style={styles.hero}>
        {/* NAV PILLS WITH ICONS */}
        <div style={styles.navPills}>
          <NavLink to="/" end style={styles.pill}>
            📊 Dashboard
          </NavLink>

          <NavLink to="/analytics" style={styles.pill}>
            📈 Analytics
          </NavLink>

          <NavLink to="/alerts" style={styles.pill}>
            🚨 Alerts
          </NavLink>

          <NavLink to="/train" style={styles.pill}>
            ⚙️ Train Model
          </NavLink>
        </div>

        {/* TITLE */}
        <h1 style={styles.heroTitle}>
          Network Anomaly Detection Using Autoencoders
        </h1>

        <p style={styles.heroSubtitle}>
          Monitor network traffic and detect anomalies using deep learning
        </p>

        {/* UPLOAD */}
        <UploadDataset setResults={setResults} />
      </div>

      {/* MAIN CONTENT */}
      <div style={styles.container}>
        {/* STATS */}
        <div style={styles.statsRow}>
          <StatsCard
            title="Total Records"
            value={total}
            icon="📊"
            navigateTo="/analytics"
          />

          <StatsCard
            title="Detected Anomalies"
            value={anomalies}
            icon="🚨"
            type="anomaly"
            navigateTo="/alerts"
          />
        </div>

        {/* GRAPH */}
        <div style={styles.card}>
          <TrafficGraph />
        </div>

        {/* ALERTS */}
        <div style={styles.card}>
          <AlertsTable alerts={results} />
        </div>
      </div>
    </div>
  );
}

/* ===================== STYLES ===================== */

const styles = {
  page: {
    minHeight: "100vh",
    background: "#f4f8ff",
  },

  hero: {
    background: "linear-gradient(180deg, #2563eb, #1e40af)",
    padding: "60px 20px",
    textAlign: "center",
    color: "#ffffff",
  },

  navPills: {
    display: "flex",
    justifyContent: "center",
    gap: "16px",
    marginBottom: "35px",
    flexWrap: "wrap",
  },

  pill: {
  padding: "10px 22px",
  borderRadius: "999px",
  background: "rgba(255,255,255,0.18)",
  color: "#ffffff",
  textDecoration: "none",
  fontWeight: "500",
  fontSize: "14px",
  display: "flex",
  alignItems: "center",
  gap: "8px",
  cursor: "pointer",
  transition: "all 0.3s ease",
},


  heroTitle: {
    fontSize: "42px",
    fontWeight: "800",
    marginBottom: "14px",
  },

  heroSubtitle: {
    fontSize: "16px",
    opacity: 0.9,
    marginBottom: "32px",
  },

  container: {
    maxWidth: "1200px",
    margin: "0 auto",
    padding: "40px 20px",
    display: "flex",
    flexDirection: "column",
    gap: "35px",
  },

  statsRow: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "30px",
  },

  card: {
    background: "#ffffff",
    borderRadius: "18px",
    padding: "26px",
    boxShadow: "0 18px 45px rgba(0,0,0,0.12)",
  },
};
