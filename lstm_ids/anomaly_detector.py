def run_detection():
    
    import numpy as np
    import pandas as pd
    import joblib
    from collections import deque
    from tensorflow.keras.models import load_model

    SEQ_LEN = 10
    THRESHOLD = 0.5

    INPUT_CSV = "data/input/test_traffic_reduced.csv"

    SCALER_PATH = "data/normalized/minmax_scaler.pkl"
    ENCODER_PATH = "autoencoder/encoder_model.h5"
    LSTM_PATH = "lstm_ids/lstm_ids_model.h5"

    print("Loading models...")
    scaler = joblib.load(SCALER_PATH)
    encoder = load_model(ENCODER_PATH, compile=False)
    lstm = load_model(LSTM_PATH, compile=False)
    print("Models loaded")

    df = pd.read_csv(INPUT_CSV)

    assert df.shape[1] == scaler.n_features_in_, (
        f"Feature mismatch: expected {scaler.n_features_in_}, got {df.shape[1]}"
    )

    X = scaler.transform(df.values.astype(np.float32))

    buffer = deque(maxlen=SEQ_LEN)
    results = []

    print("\n Anomaly Detection Started\n")

    for i in range(len(X)):
        buffer.append(X[i])

        if len(buffer) == SEQ_LEN:
            seq = np.array(buffer).reshape(1, -1)

            encoded = encoder.predict(seq, verbose=0)
            encoded = encoded.reshape(1, 1, -1)

            score = lstm.predict(encoded, verbose=0)[0][0]
            label = 1 if score > THRESHOLD else 0

            results.append({
                "index": i,
                "anomaly_score": round(float(score), 4),
                "prediction": "Anomaly" if label == 1 else "Normal"
            })

            print(
                f"Index {i:5d} | "
                f"Score = {score:.3f} | "
                f"{'Anomaly' if label else 'Normal'}"
            )

    out_df = pd.DataFrame(results)
    out_df.to_csv("data/output/anomaly_results.csv", index=False)

    print("\n Results saved to data/output/anomaly_results.csv")

if __name__ == "__main__":
    run_detection()