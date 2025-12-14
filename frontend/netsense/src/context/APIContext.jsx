import { createContext, useContext } from "react";
import axios from "axios";

/**
 * Central API configuration
 */
const APIContext = createContext();

const API_BASE_URL = "http://127.0.0.1:8000/api";

const api = axios.create({
  baseURL: API_BASE_URL,
});

/**
 * API Provider
 */
export const APIProvider = ({ children }) => {
  // Detect anomalies
  const detectAnomaly = async (formData) => {
    const response = await api.post("/detect/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  };

  // Fetch anomaly alerts
  const fetchAlerts = async () => {
    const response = await api.get("/alerts/");
    return response.data;
  };

  return (
    <APIContext.Provider
      value={{
        detectAnomaly,
        fetchAlerts,
      }}
    >
      {children}
    </APIContext.Provider>
  );
};

// Custom hook for easy usage
export const useAPI = () => {
  return useContext(APIContext);
};
