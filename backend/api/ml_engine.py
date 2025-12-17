import numpy as np
import tensorflow as tf
import pickle
import os
import pandas as pd
from django.conf import settings

# =====================================================
# Paths (ML folder is OUTSIDE backend)
# =====================================================
BASE_DIR = settings.BASE_DIR                 # backend/
PROJECT_ROOT = os.path.dirname(BASE_DIR)     # NetSense/

MODEL_DIR = os.path.join(PROJECT_ROOT, "ml", "models")

MODEL_PATH = os.path.join(MODEL_DIR, "lstm_autoencoder.h5")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "encoders.pkl")

# =====================================================
# Load model, scaler, encoders
# =====================================================
model = tf.keras.models.load_model(MODEL_PATH, compile=False)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoders = pickle.load(f)

FEATURE_ORDER = list(scaler.feature_names_in_)  # exact training order

# =====================================================
# Inference
# =====================================================
def run_inference(raw_features: dict):
    """
    raw_features: dict from API (features JSON)
    """

    # -----------------------------------------
    # Convert to DataFrame (IMPORTANT FIX)
    # -----------------------------------------
    df = pd.DataFrame([raw_features])

    # -----------------------------------------
    # Encode categorical columns
    # -----------------------------------------
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col].astype(str))
        else:
            # Missing categorical → default 0
            df[col] = 0

    # -----------------------------------------
    # Ensure all features exist (NO KeyError)
    # -----------------------------------------
    for col in FEATURE_ORDER:
        if col not in df.columns:
            df[col] = 0

    # -----------------------------------------
    # Reorder columns EXACTLY like training
    # -----------------------------------------
    df = df[FEATURE_ORDER]

    # -----------------------------------------
    # Scale
    # -----------------------------------------
    x_scaled = scaler.transform(df)

    # -----------------------------------------
    # LSTM expects 3D
    # -----------------------------------------
    x_lstm = x_scaled.reshape(1, 1, x_scaled.shape[1])

    # -----------------------------------------
    # Predict
    # -----------------------------------------
    reconstructed = model.predict(x_lstm, verbose=0)

    mse = float(np.mean((x_lstm - reconstructed) ** 2))
    is_anomaly = mse > 0.01

    # -----------------------------------------
    # Return SAFE python types
    # -----------------------------------------
    return df.iloc[0].to_dict(), mse, is_anomaly
