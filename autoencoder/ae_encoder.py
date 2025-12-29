import numpy as np
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.layers import Input

AE_MODEL_PATH = "autoencoder/best_ae_model.h5"
ENCODER_MODEL_PATH = "autoencoder/encoder_model.h5"

X_SEQ_PATH = "data/sequences/X_sequences.npy"
Y_SEQ_PATH = "data/sequences/y_sequences.npy"

OUTPUT_X = "data/sequences/X_encoded.npy"
OUTPUT_Y = "data/sequences/y_encoded.npy"

BATCH_SIZE = 1024

autoencoder = load_model(AE_MODEL_PATH, compile=False)

# Encoder = output of the first Dense layer
encoder = Model(
    inputs=autoencoder.input,
    outputs=autoencoder.layers[1].output
)

encoder.save(ENCODER_MODEL_PATH)
print("Encoder model saved.")

X_seq = np.load(X_SEQ_PATH, mmap_mode='r')
y_seq = np.load(Y_SEQ_PATH)

X_flat = X_seq.reshape(X_seq.shape[0], -1).astype(np.float32)

encoded_batches = []

for i in range(0, X_flat.shape[0], BATCH_SIZE):
    batch = X_flat[i:i + BATCH_SIZE]
    encoded = encoder.predict(batch, verbose=0)
    encoded_batches.append(encoded)

X_encoded = np.vstack(encoded_batches)

np.save(OUTPUT_X, X_encoded)
np.save(OUTPUT_Y, y_seq)

print("Encoded features saved.")
print("Encoded shape:", X_encoded.shape)
