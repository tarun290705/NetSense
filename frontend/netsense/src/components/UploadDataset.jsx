export default function UploadDataset({ setResults }) {
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // For now just demo result (replace with API call later)
    console.log("Selected file:", file.name);

    // Example mock result
    setResults([
      { is_anomaly: false },
      { is_anomaly: true },
      { is_anomaly: false },
    ]);
  };

  return (
    <div style={styles.wrapper}>
      <label style={styles.uploadBox}>
        📁 Upload Network Traffic File
        <input
          type="file"
          accept=".csv"
          hidden
          onChange={handleFileChange}
        />
      </label>
    </div>
  );
}

const styles = {
  wrapper: {
    display: "flex",
    justifyContent: "center",
    marginBottom: "30px",
  },

  uploadBox: {
    background: " #2563eb",
    color: "#ffffff",
    padding: "16px 28px",
    borderRadius: "12px",
    fontSize: "16px",
    fontWeight: "500",
    cursor: "pointer",
    boxShadow: "0 8px 18px rgba(2,6,23,0.4)",
    transition: "transform 0.2s ease",
  },
};
