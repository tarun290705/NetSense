import os
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

from utils.preprocessing import (
    drop_unused_columns,
    encode_categorical,
)


DATA_PATH = "data/raw/UNSW_NB15_training-set.csv"
SCALER_PATH = "models/scaler.pkl"
MODEL_PATH = "models/lstm_autoencoder.h5"


# -------------------------
# Build LSTM Autoencoder
# -------------------------
def build_lstm_autoencoder(n_features):

    inputs = tf.keras.Input(shape=(1, n_features))

    # Encoder
    x = tf.keras.layers.LSTM(64, return_sequences=False)(inputs)
    latent = tf.keras.layers.RepeatVector(1)(x)

    # Decoder
    x = tf.keras.layers.LSTM(64, return_sequences=True)(latent)
    outputs = tf.keras.layers.TimeDistributed(
        tf.keras.layers.Dense(n_features)
    )(x)

    model = tf.keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mse")

    model.summary()
    return model


# -------------------------
# Load + preprocess data
# -------------------------
def load_and_prepare_data(path):
    df = pd.read_csv(path)

    df = drop_unused_columns(df)
    df, encoders = encode_categorical(df)

    with open("models/encoders.pkl", "wb") as f:
        pickle.dump(encoders, f)


    # Scale numeric data
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    # Save scaler for inference
    with open(SCALER_PATH, "wb") as f:
        pickle.dump(scaler, f)

    # Reshape for LSTM: (samples, timesteps=1, features)
    X = scaled.reshape((scaled.shape[0], 1, scaled.shape[1]))

    return X, df.shape[1]


# -------------------------
# Training script
# -------------------------
def main():

    print("\nLoading and preparing dataset...")
    X, n_features = load_and_prepare_data(DATA_PATH)

    print(f"Dataset loaded. Feature count = {n_features}")

    print("\nBuilding model...")
    model = build_lstm_autoencoder(n_features)

    print("\nTraining model...")
    model.fit(
        X, X,                       # Autoencoder targets = inputs
        epochs=50,
        batch_size=32,
        validation_split=0.2,
        shuffle=True,
        verbose=1
    )

    print("\nSaving model...")
    os.makedirs("models", exist_ok=True)
    model.save(MODEL_PATH)

    print("\nTraining complete! Model saved.")


if __name__ == "__main__":
    main()
