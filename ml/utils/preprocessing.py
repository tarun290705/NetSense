import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# ---------------------------
# 1. Drop unused columns
# ---------------------------
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


# ---------------------------
# 2. Encode categorical columns (e.g., protocol, service, flag)
# ---------------------------
def encode_categorical(df):
    encoders = {}
    cat_cols = ["proto"]

    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df, encoders



# ---------------------------
# 3. Scale numeric data
# ---------------------------
def scale_data(df: pd.DataFrame):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    # Save scaler
    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    return scaled
