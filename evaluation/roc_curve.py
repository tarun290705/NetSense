import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import load_model

model = load_model("lstm_ids/lstm_ids_model.h5", compile=False)

X = np.load("data/sequences/X_encoded.npy")
y = np.load("data/sequences/y_encoded.npy")

X = X.reshape(X.shape[0], 1, X.shape[1])

y_prob = model.predict(X, verbose=0)

fpr, tpr, _ = roc_curve(y, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.4f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
