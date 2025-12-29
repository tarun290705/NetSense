from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import Adam

def build_autoencoder(input_dim, hidden_dim, dropout_rate, learning_rate):
    # Encoder
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(hidden_dim, activation='relu')(input_layer)
    encoded = Dropout(dropout_rate)(encoded)

    # Decoder
    decoded = Dense(input_dim, activation='linear')(encoded)

    autoencoder = Model(inputs=input_layer, outputs=decoded)

    autoencoder.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss='mse'
    )

    return autoencoder
