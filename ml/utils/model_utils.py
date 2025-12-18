from keras.models import Model
from keras.layers import Input, LSTM, RepeatVector, TimeDistributed, Dense

def build_lstm_autoencoder(timesteps, n_features):
    inputs = Input(shape=(timesteps, n_features))

    encoded = LSTM(32, activation="relu")(inputs)
    encoded = Dense(16, activation="relu")(encoded)

    bottleneck = Dense(8, activation="relu")(encoded)

    decoded = Dense(16, activation="relu")(bottleneck)
    decoded = Dense(32, activation="relu")(decoded)
    decoded = RepeatVector(timesteps)(decoded)
    decoded = LSTM(32, activation="relu", return_sequences=True)(decoded)

    outputs = TimeDistributed(Dense(n_features))(decoded)

    model = Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mse")
    return model
