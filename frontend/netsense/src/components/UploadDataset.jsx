
import { useRef, useState } from "react";

export default function UploadDataset() {
  const fileInputRef = useRef(null);
  const [fileName, setFileName] = useState("");

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
      console.log("Selected file:", file);
      // later: send file to backend
    }
  };

  return (
    <div className="card">
      <h3>Upload Network Traffic</h3>
      <p>Upload CSV file to detect anomalies</p>

      {/* Hidden file input */}
      <input
        type="file"
        accept=".csv"
        ref={fileInputRef}
        onChange={handleFileChange}
        style={{ display: "none" }}
      />

      {/* Styled button */}
      <button className="primary-btn" onClick={handleButtonClick}>
        Upload File
      </button>

      {/* Show selected file */}
      {fileName && (
        <p style={{ marginTop: "10px", fontSize: "14px", color: "#555" }}>
          Selected: <strong>{fileName}</strong>
        </p>
      )}
    </div>
  );
}
