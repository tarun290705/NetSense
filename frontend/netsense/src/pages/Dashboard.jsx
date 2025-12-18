import { useState } from "react";
import Sidebar from "../components/Sidebar";

export default function Dashboard() {
  const [sourceIP, setSourceIP] = useState("");
  const [destIP, setDestIP] = useState("");
  const [protocol, setProtocol] = useState("");
  const [packetLength, setPacketLength] = useState("");

  const [errors, setErrors] = useState({});

  // IPv4 validation regex
  const ipRegex =
    /^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$/;

  const validateForm = () => {
    let newErrors = {};

    if (!ipRegex.test(sourceIP)) {
      newErrors.sourceIP = "Invalid Source IP address";
    }

    if (!ipRegex.test(destIP)) {
      newErrors.destIP = "Invalid Destination IP address";
    }

    if (!protocol) {
      newErrors.protocol = "Please select a protocol";
    }

    if (!packetLength || packetLength <= 0) {
      newErrors.packetLength = "Packet length must be greater than 0";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    // Phase 3 → API call will be added here
    console.log("Traffic Data:", {
      sourceIP,
      destIP,
      protocol,
      packetLength,
    });

    alert("Traffic data is valid ✔️");
  };

  return (
    <div className="layout">
      <Sidebar />

      <main className="main">
        <div className="navbar">
          <h3>Network Anomaly Detection Using Autoencoder</h3>
        </div>

        <div className="form-card">
          <h2>Enter Network Traffic Details</h2>

          <form className="traffic-form" onSubmit={handleSubmit}>
            {/* Row 1 */}
            <div className="form-row">
              <div className="form-group">
                <label>Source IP Address</label>
                <input
                  type="text"
                  value={sourceIP}
                  onChange={(e) => setSourceIP(e.target.value)}
                  placeholder="e.g. 192.168.1.10"
                />
                {errors.sourceIP && (
                  <span className="error-text">{errors.sourceIP}</span>
                )}
              </div>

              <div className="form-group">
                <label>Destination IP Address</label>
                <input
                  type="text"
                  value={destIP}
                  onChange={(e) => setDestIP(e.target.value)}
                  placeholder="e.g. 192.168.1.20"
                />
                {errors.destIP && (
                  <span className="error-text">{errors.destIP}</span>
                )}
              </div>
            </div>

            {/* Row 2 */}
            <div className="form-row">
              <div className="form-group">
                <label>Protocol</label>
                <select
                  value={protocol}
                  onChange={(e) => setProtocol(e.target.value)}
                >
                  <option value="">Select Protocol</option>
                  <option value="TCP">TCP</option>
                  <option value="UDP">UDP</option>
                </select>
                {errors.protocol && (
                  <span className="error-text">{errors.protocol}</span>
                )}
              </div>

              <div className="form-group">
                <label>Packet Length</label>
                <input
                  type="number"
                  value={packetLength}
                  onChange={(e) => setPacketLength(e.target.value)}
                  placeholder="e.g. 512"
                />
                {errors.packetLength && (
                  <span className="error-text">{errors.packetLength}</span>
                )}
              </div>
            </div>

            <button type="submit" className="primary-btn half-width">
              Analyze Traffic
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}
