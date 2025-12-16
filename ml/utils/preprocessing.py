import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# ---------------------------
# 1. Drop unused columns
# ---------------------------
def drop_unused_columns(df: pd.DataFrame):
    cols_to_drop = ["label", "difficulty", "id", "attack_cat"]
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors="ignore")
    return df

# ---------------------------
# 2. Encode categorical columns (e.g., protocol, service, flag)
# ---------------------------
def encode_categorical(df):
    from sklearn.preprocessing import LabelEncoder
    
    encoders = {}
    cat_cols = df.select_dtypes(include=["object"]).columns

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
