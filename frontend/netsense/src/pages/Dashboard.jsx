import Sidebar from "../components/Sidebar";

export default function Dashboard() {
  return (
    <div className="layout">
      <Sidebar />

      <main className="main">
        {/* Header */}
        <div className="navbar">
          <h3>Network Anomaly Detection Using Autoencoder</h3>
        </div>

        {/* Form Card */}
        <div className="form-card">
          <h2>Enter Network Traffic Details</h2>

          <form className="traffic-form">
            {/* Row 1 */}
            <div className="form-row">
              <div className="form-group">
                <label>Source IP Address</label>
                <input type="text" placeholder="e.g. 192.168.1.10" />
              </div>

              <div className="form-group">
                <label>Destination IP Address</label>
                <input type="text" placeholder="e.g. 192.168.1.20" />
              </div>
            </div>

            {/* Row 2 */}
            <div className="form-row">
              <div className="form-group">
                <label>Protocol</label>
                <select>
                  <option value="">Select Protocol</option>
                  <option value="TCP">TCP</option>
                  <option value="UDP">UDP</option>
                </select>
              </div>

              <div className="form-group">
                <label>Packet Length</label>
                <input type="number" placeholder="e.g. 512" />
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
