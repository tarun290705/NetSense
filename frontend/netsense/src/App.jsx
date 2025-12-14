import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Analytics from "./pages/Analytics";
import Alerts from "./pages/Alerts";
import TrainModel from "./pages/TrainModel";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/analytics" element={<Analytics />} />
      <Route path="/alerts" element={<Alerts />} />
      <Route path="/train" element={<TrainModel />} />
    </Routes>
  );
}
