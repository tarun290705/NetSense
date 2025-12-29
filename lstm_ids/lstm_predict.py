import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

model = load_model("lstm_ids/lstm_ids_model.h5")

X = np.load("data/sequences/X_encoded.npy")
y = np.load("data/sequences/y_encoded.npy")

X = X.reshape(X.shape[0], 1, X.shape[1])

y_pred_prob = model.predict(X, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int)

print(classification_report(y, y_pred))
print("ROC-AUC:", roc_auc_score(y, y_pred_prob))
