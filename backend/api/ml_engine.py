import numpy as np
import tensorflow as tf
import pickle
import os
import pandas as pd
from django.conf import settings
from collections import deque

MSE_BUFFER = deque(maxlen=500)
WARMUP_SIZE = 100   # 🔑 important

BASE_DIR = settings.BASE_DIR
PROJECT_ROOT = os.path.dirname(BASE_DIR)

MODEL_DIR = os.path.join(PROJECT_ROOT, "ml", "models")

MODEL_PATH = os.path.join(MODEL_DIR, "lstm_autoencoder.h5")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "encoders.pkl")

model = tf.keras.models.load_model(MODEL_PATH, compile=False)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoders = pickle.load(f)

FEATURE_ORDER = list(scaler.feature_names_in_)

def run_inference(raw_features: dict):
    df = pd.DataFrame([raw_features])

    for col, encoder in encoders.items():
        if col in df.columns:
            try:
                df[col] = encoder.transform(df[col].astype(str))
            except ValueError:
                df[col] = 0
        else:
            df[col] = 0

    for col in FEATURE_ORDER:
        if col not in df.columns:
            df[col] = 0

    df = df[FEATURE_ORDER]

    x_scaled = scaler.transform(df)
    x_lstm = x_scaled.reshape(1, 1, x_scaled.shape[1])

    reconstructed = model.predict(x_lstm, verbose=0)
    mse = float(np.mean((x_lstm - reconstructed) ** 2))

    MSE_BUFFER.append(mse)

    MIN_BUFFER = 50     
    STD_FACTOR = 3      

    if len(MSE_BUFFER) < MIN_BUFFER:
        threshold = None
        is_anomaly = False
    else:
        mean = np.mean(MSE_BUFFER)
        std = np.std(MSE_BUFFER)
        threshold = mean + STD_FACTOR * std
        is_anomaly = mse > threshold

    return df.iloc[0].to_dict(), mse, is_anomaly, threshold
