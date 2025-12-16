import numpy as np
import tensorflow as tf
import pickle
import os
from django.conf import settings

# ---------------------------------------------
# Correct absolute paths (ML folder OUTSIDE backend)
# ---------------------------------------------
BASE_DIR = settings.BASE_DIR  # Points to backend/ folder
PROJECT_ROOT = os.path.dirname(BASE_DIR)  # One level up (Net Sense/)

MODEL_DIR = os.path.join(PROJECT_ROOT, "ml", "models")

MODEL_PATH = os.path.join(MODEL_DIR, "lstm_autoencoder.h5")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "encoders.pkl")

# ---------------------------------------------
# Load model and scaler safely
# ---------------------------------------------
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"MODEL NOT FOUND: {MODEL_PATH}")

if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError(f"SCALER NOT FOUND: {SCALER_PATH}")

model = tf.keras.models.load_model(MODEL_PATH, compile=False)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoders = pickle.load(f)

# Number of features used during training
EXPECTED_FEATURES = scaler.n_features_in_


# ---------------------------------------------
# Main inference function
# ---------------------------------------------
def run_inference(feature_dict):

    # Encode categorical values
    for col, encoder in encoders.items():
        if col in feature_dict:
            feature_dict[col] = encoder.transform([feature_dict[col]])[0]

    # Order features exactly as training
    ordered = [feature_dict[f] for f in scaler.feature_names_in_]

    x = np.array(ordered, dtype=float).reshape(1, -1)
    x_scaled = scaler.transform(x)
    x_lstm = x_scaled.reshape(1, 1, x_scaled.shape[1])

    reconstructed = model.predict(x_lstm)
    mse = float(np.mean((x_lstm - reconstructed) ** 2))
    anomaly = mse > 0.01

    return ordered, mse, anomaly
