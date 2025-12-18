import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pickle
import os

def drop_unused_columns(df):
    keep_cols = [
        "dur",
        "proto",
        "spkts",
        "dpkts",
        "sbytes",
        "dbytes"
    ]
    return df[keep_cols]

def encode_categorical(df):
    encoders = {}
    cat_cols = ["proto"]

    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df, encoders

def scale_data(df: pd.DataFrame):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    return scaled
