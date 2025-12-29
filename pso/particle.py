import numpy as np

BOUNDS = {
    'hidden_dim': (16, 128),
    'learning_rate': (0.0001, 0.01),
    'dropout_rate': (0.1, 0.5),
    'batch_size': (16, 128)
}

def generate_particle():
    return np.array([
        np.random.randint(*BOUNDS['hidden_dim']),
        np.random.uniform(*BOUNDS['learning_rate']),
        np.random.uniform(*BOUNDS['dropout_rate']),
        np.random.randint(*BOUNDS['batch_size'])
    ])
