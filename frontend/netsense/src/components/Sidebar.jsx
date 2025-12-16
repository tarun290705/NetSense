import { useState } from "react";
import { NavLink } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <h2 className="logo">NetSense</h2>

      <nav className="menu">
        <NavLink to="/" end>📊 Dashboard</NavLink>
        <NavLink to="/analytics">📈 Analytics</NavLink>
        <NavLink to="/alerts">🚨 Alerts</NavLink>
       <NavLink to="/logHistory">📑 Log History</NavLink>
      </nav>
    </aside>
  );
}
