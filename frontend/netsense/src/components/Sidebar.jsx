import { useState } from "react";
import { NavLink } from "react-router-dom";

export default function Sidebar() {
  return (
    <div style={styles.sidebar}>
      <h1 style={styles.logo}>NetSense</h1>

      <NavItem to="/" icon="📊" label="Dashboard" />
      <NavItem to="/analytics" icon="📈" label="Analytics" />
      <NavItem to="/alerts" icon="🚨" label="Alerts" />
      <NavItem to="/train" icon="⚙️" label="Train Model" />
    </div>
  );
}

function NavItem({ to, icon, label }) {
  return (
    <NavLink
      to={to}
      style={({ isActive }) => ({
        ...styles.card,
        background: isActive
          ? "rgba(255,255,255,0.25)"
          : "rgba(255,255,255,0.15)",
      })}
    >
      <span style={styles.icon}>{icon}</span>
      <span>{label}</span>
      <span style={styles.arrow}>›</span>
    </NavLink>
  );
}

const styles = {
  sidebar: {
    width: "240px",
    height: "100vh",
    padding: "24px 18px",
    background: "linear-gradient(180deg, #2563eb, #3b82f6)",
    color: "#ffffff",
  },

  logo: {
    fontSize: "26px",
    fontWeight: "800",
    marginBottom: "30px",
  },

card: {
  display: "flex",
  alignItems: "center",
  gap: "12px",
  padding: "14px 18px",
  marginBottom: "14px",
  borderRadius: "14px",
  background: "rgba(255,255,255,0.18)",
  textDecoration: "none",
  color: "#ffffff",
  boxShadow: "0 6px 14px rgba(0,0,0,0.25)",
},


  icon: {
    fontSize: "18px",
  },

  arrow: {
    marginLeft: "auto",
    fontSize: "18px",
    opacity: 0.8,
  },
};
