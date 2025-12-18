import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle
from utils.preprocessing import drop_unused_columns

MODEL_PATH = "models/lstm_autoencoder.h5"
SCALER_PATH = "models/scaler.pkl"

def load_scaler():
    with open(SCALER_PATH, "rb") as f:
        return pickle.load(f)

def detect_anomaly(df):
    df = drop_unused_columns(df)

    scaler = load_scaler()
    scaled = scaler.transform(df)

    model = load_model(MODEL_PATH)

    timesteps = 10
    X = []

    for i in range(len(scaled) - timesteps):
        X.append(scaled[i:i+timesteps])

    X = np.array(X)

    recon = model.predict(X)
    loss = np.mean((recon - X) ** 2, axis=(1, 2))

    threshold = np.percentile(loss, 95)

    anomalies = loss > threshold
    return anomalies, loss, threshold
