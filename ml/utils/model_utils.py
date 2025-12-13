from keras.models import Model
from keras.layers import Input, LSTM, RepeatVector, TimeDistributed, Dense

def build_lstm_autoencoder(timesteps, n_features):
    inputs = Input(shape=(timesteps, n_features))

    # Encoder
    encoded = LSTM(32, activation="relu")(inputs)
    encoded = Dense(16, activation="relu")(encoded)

    # Bottleneck
    bottleneck = Dense(8, activation="relu")(encoded)

    # Decoder
    decoded = Dense(16, activation="relu")(bottleneck)
    decoded = Dense(32, activation="relu")(decoded)
    decoded = RepeatVector(timesteps)(decoded)
    decoded = LSTM(32, activation="relu", return_sequences=True)(decoded)

    # IMPORTANT: final output dimension must match n_features
    outputs = TimeDistributed(Dense(n_features))(decoded)

    model = Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mse")
    return model
