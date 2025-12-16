import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import UploadDataset from "../components/UploadDataset";
import TrafficGraph from "../components/TrafficGraph";

export default function Dashboard() {
  return (
    <div className="layout">
      <Sidebar />

      <main className="main">
        <Navbar />

        <section className="stats-row">
          <StatsCard title="Total Records" value="0" icon="📦" />
          <StatsCard title="Detected Anomalies" value="0" icon="🚨" />
        </section>

        <section className="grid">
          <UploadDataset />
          <TrafficGraph />
        </section>
      </main>
    </div>
  );
}
