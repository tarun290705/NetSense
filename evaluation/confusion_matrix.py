import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import load_model

# Load model and data
model = load_model("lstm_ids/lstm_ids_model.h5", compile=False)

X = np.load("data/sequences/X_encoded.npy")
y = np.load("data/sequences/y_encoded.npy")

X = X.reshape(X.shape[0], 1, X.shape[1])

# Predictions
y_prob = model.predict(X, verbose=0)
y_pred = (y_prob > 0.5).astype(int)

# Confusion matrix
cm = confusion_matrix(y, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.colorbar()

plt.xticks([0, 1], ["Normal", "Anomaly"])
plt.yticks([0, 1], ["Normal", "Anomaly"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.show()
