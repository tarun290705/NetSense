export default function StatsCard({ title, value, icon }) {
  return (
    <div className="stats-card">
      <div>
        <p>{title}</p>
        <h2>{value}</h2>
      </div>
      <span className="stats-icon">{icon}</span>
    </div>
  );
}
