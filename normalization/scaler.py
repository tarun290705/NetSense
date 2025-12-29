import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

INPUT_PATH = "data/flows/clean_flows.csv"
OUTPUT_PATH = "data/normalized/normalized_flows.csv"
SCALER_PATH = "data/normalized/minmax_scaler.pkl"

def load_data(path):
    df = pd.read_csv(path)
    return df

def split_features_labels(df):
    X = df.drop(columns=['Label'])
    y = df['Label']
    return X, y

def normalize_features(X):
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler

def combine_scaled_data(X_scaled, y, feature_names):
    df_scaled = pd.DataFrame(X_scaled, columns=feature_names)
    df_scaled['Label'] = y.values
    return df_scaled

def save_outputs(df_scaled, scaler):
    df_scaled.to_csv(OUTPUT_PATH, index=False)
    joblib.dump(scaler, SCALER_PATH)
    print("Normalized data and scaler saved successfully.")

if __name__ == "__main__":
    df = load_data(INPUT_PATH)

    X, y = split_features_labels(df)

    X_scaled, scaler = normalize_features(X)

    df_scaled = combine_scaled_data(X_scaled, y, X.columns)

    save_outputs(df_scaled, scaler)
