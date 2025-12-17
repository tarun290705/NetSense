import requests

API_URL = "http://127.0.0.1:8000/api/logs/"

def send_log(payload):
    try:
        response = requests.post(API_URL, json=payload, timeout=3)
        print("✔ Sent:", response.json())
    except Exception as e:
        print("❌ Failed to send:", e)
