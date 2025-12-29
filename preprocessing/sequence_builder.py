import pandas as pd
import numpy as np

INPUT_PATH = "data/normalized/normalized_flows.csv"
OUTPUT_DIR = "data/sequences/"

SEQUENCE_LENGTH = 10

def load_data(path):
    return pd.read_csv(path)

def split_features_labels(df):
    X = df.drop(columns=['Label']).values
    y = df['Label'].values
    return X, y

def create_sequences(X, y, seq_length):
    X_seq = []
    y_seq = []

    for i in range(len(X) - seq_length):
        X_seq.append(X[i:i + seq_length])
        y_seq.append(y[i + seq_length])

    return np.array(X_seq), np.array(y_seq)

def save_sequences(X_seq, y_seq, output_dir):
    np.save(output_dir + "X_sequences.npy", X_seq)
    np.save(output_dir + "y_sequences.npy", y_seq)
    print("Sequences saved successfully.")

if __name__ == "__main__":
    df = load_data(INPUT_PATH)

    X, y = split_features_labels(df)

    X_seq, y_seq = create_sequences(X, y, SEQUENCE_LENGTH)

    save_sequences(X_seq, y_seq, OUTPUT_DIR)

    print("X shape:", X_seq.shape)
    print("y shape:", y_seq.shape)
