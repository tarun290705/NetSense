import numpy as np
from tensorflow.keras.models import save_model
from pso.swarm import run_pso
from autoencoder.ae_model import build_autoencoder

def main():
    y_seq = np.load("data/sequences/y_sequences.npy")

    normal_indices = np.where(y_seq == 0)[0]

    MAX_SAMPLES = 50000
    if len(normal_indices) > MAX_SAMPLES:
        selected_indices = np.random.choice(
            normal_indices, MAX_SAMPLES, replace=False
        )
    else:
        selected_indices = normal_indices

    X_seq = np.load("data/sequences/X_sequences.npy", mmap_mode='r')

    X_seq = X_seq[selected_indices].astype(np.float32)

    X_flat = X_seq.reshape(X_seq.shape[0], -1)

    best_particle = run_pso(X_flat)

    hidden_dim, lr, dropout, batch_size = best_particle

    model = build_autoencoder(
        input_dim=X_flat.shape[1],
        hidden_dim=int(hidden_dim),
        dropout_rate=dropout,
        learning_rate=lr
    )

    model.fit(
        X_flat, X_flat,
        epochs=20,
        batch_size=int(batch_size),
        verbose=1
    )

    save_model(model, "autoencoder/best_ae_model.h5")
    print("Best autoencoder saved.")

if __name__ == "__main__":
    main()
