import numpy as np
from autoencoder.ae_model import build_autoencoder

def fitness_function(particle, X_train):
    hidden_dim = int(particle[0])
    learning_rate = particle[1]
    dropout_rate = particle[2]
    batch_size = int(particle[3])

    model = build_autoencoder(
        input_dim=X_train.shape[1],
        hidden_dim=hidden_dim,
        dropout_rate=dropout_rate,
        learning_rate=learning_rate
    )

    history = model.fit(
        X_train, X_train,
        epochs=5,
        batch_size=batch_size,
        verbose=0
    )

    loss = history.history['loss'][-1]
    return loss
