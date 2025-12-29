import numpy as np
from sklearn.model_selection import train_test_split
from lstm_ids.lstm_model import build_lstm
from tensorflow.keras.models import save_model

X = np.load("data/sequences/X_encoded.npy")
y = np.load("data/sequences/y_encoded.npy")

X = X.reshape(X.shape[0], 1, X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = build_lstm(input_shape=(X.shape[1], X.shape[2]))

history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=512,
    validation_split=0.1,
    verbose=1
)

save_model(model, "lstm_ids/lstm_ids_model.h5")
print("LSTM IDS model saved.")

import matplotlib.pyplot as plt

plt.figure()
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("LSTM Training Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("LSTM Accuracy")
plt.legend()
plt.show()
