import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

X_PATH = "data/sequences/X_encoded.npy"
Y_PATH = "data/sequences/y_encoded.npy"

LSTM_MODEL_PATH = "lstm_ids/lstm_ids_model.h5"

THRESHOLD = 0.5
BATCH_SIZE = 256

print("[+] Loading encoded data...")
X = np.load(X_PATH, mmap_mode="r")  
y_true = np.load(Y_PATH, mmap_mode="r")

print(f"[✓] X shape (raw): {X.shape}")
print(f"[✓] y shape: {y_true.shape}")

print("[+] Loading LSTM model...")
lstm_model = load_model(LSTM_MODEL_PATH, compile=False)
print("[✓] Model loaded")

print("[+] Running batch-wise predictions...")

y_pred = []
num_samples = len(X)

for start in range(0, num_samples, BATCH_SIZE):
    end = min(start + BATCH_SIZE, num_samples)

    X_batch = X[start:end]

    X_batch = X_batch.reshape(X_batch.shape[0], 1, X_batch.shape[1])

    scores = lstm_model.predict(X_batch, verbose=0).flatten()
    preds = (scores > THRESHOLD).astype(int)

    y_pred.extend(preds)

    if start % (BATCH_SIZE * 20) == 0:
        print(f"  Processed {end}/{num_samples} samples")

y_pred = np.array(y_pred)

accuracy = accuracy_score(y_true[:len(y_pred)], y_pred)

print("\nMODEL ACCURACY (Encoded Sequences)")
print(f"Accuracy: {accuracy:.4f}")
