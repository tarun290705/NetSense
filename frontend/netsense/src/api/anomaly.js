import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

export const detectAnomaly = async (formData) => {
  return await axios.post(`${BASE_URL}/detect/`, formData);
};

export const fetchAlerts = async () => {
  return await axios.get(`${BASE_URL}/alerts/`);
};
