# NetSense — Network Sensing & Anomaly Detection

NetSense is a modular project for capturing network traffic, building flow-level features, training an LSTM autoencoder anomaly detection model, and serving predictions via a Django backend API.

This README documents the system, repository layout, setup, and usage for each component so you can run, train, and deploy the system locally.

---

## Key Concepts

- Purpose: Capture network flows, extract features, detect anomalous network behavior with an LSTM autoencoder, and expose predictions via a REST API.
- Components: Data capture (packet sniffer and flow tracker), ML training/inference, and a Django backend API.

---

## Repository Structure

- `backend/` — Django project and `api` app providing endpoints and model-serving logic.
  - See [backend/manage.py](backend/manage.py) and the app in [backend/api](backend/api)
- `ml/` — Training and inference scripts, model artifacts, and utilities.
  - Key files: [ml/train.py](ml/train.py), [ml/inference.py](ml/inference.py), [ml/utils](ml/utils)
  - Models: `ml/models/lstm_autoencoder.h5`
- `data_capture/` — Packet sniffer, feature builder, flow tracker, and sender for forwarding features to the backend.
  - Entry: [data_capture/main.py](data_capture/main.py)
  - Capture helpers: [data_capture/capture](data_capture/capture)
  - Sender: [data_capture/sender/send_to_backend.py](data_capture/sender/send_to_backend.py)
- `requirements.txt` — Python dependencies for the project environment.

---

## Component Details

1) Backend (Django)

- Location: `backend/`
- Purpose: Receive feature payloads from data capture, perform any preprocessing, and return predictions from the trained ML model. Also hosts any management/admin endpoints.
- Important files:
  - [backend/manage.py](backend/manage.py) — Django cli entry.
  - [backend/api/views.py](backend/api/views.py) — API views (prediction endpoint logic).
  - [backend/api/serializers.py](backend/api/serializers.py) — Input serialization and validation.
  - [backend/netsense/settings.py](backend/netsense/settings.py) — Django settings, including installed apps and model config.

2) Machine Learning

- Location: `ml/`
- Training: `ml/train.py` loads the raw UNSW dataset `ml/data/raw/UNSW_NB15_training-set.csv`, preprocesses features using utilities in `ml/utils/`, scales features with `StandardScaler`, trains an LSTM autoencoder and saves:
  - Model: `ml/models/lstm_autoencoder.h5`
  - Scaler: `ml/models/scaler.pkl`
  - Encoders: `ml/models/encoders.pkl`

- Inference: `ml/inference.py` loads saved model + scaler + encoders and exposes functions to convert incoming feature payloads into model-ready input and compute reconstruction error / anomaly scores.

3) Data Capture

- Location: `data_capture/`
- Purpose: Capture packets/flows, extract features consistent with training pipeline, and upload features to the backend API.
- Key modules:
  - `data_capture/capture/packet_sniffer.py` — captures packets from interfaces.
  - `data_capture/capture/flow_tracker.py` — groups packets into flows.
  - `data_capture/capture/feature_builder.py` — builds numerical features per flow consistent with training preprocessing.
  - `data_capture/sender/send_to_backend.py` — HTTP client to POST features to the backend ingestion/prediction endpoint.

---

## Setup & Installation

1. Create and activate a virtual environment (Windows example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

2. (Optional) If you only need to run training/inference, install ML-specific deps in `requirements.txt`.

3. Ensure dataset files exist:
- `ml/data/raw/UNSW_NB15_training-set.csv` and `ml/data/raw/UNSW_NB15_testing-set.csv` are included in `ml/data/raw/`.

4. Create a `models/` directory at the repository root or ensure `ml/models/` exists before training (scripts create theirs if needed).

---

## Running the Components

1) Train the model

```bash
python ml/train.py
```

- What it does: preprocesses the training CSV, fits encoders + scaler, trains the LSTM autoencoder, and saves the model and preprocessing artifacts under `ml/models/` (see variables inside the script: `MODEL_PATH`, `SCALER_PATH`).

2) Run inference locally (example usage)

```bash
python ml/inference.py
```

- `inference.py` contains helper functions to load `ml/models/lstm_autoencoder.h5` and `ml/models/scaler.pkl` and score incoming feature vectors.

3) Run the backend API server

```bash
cd backend
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

- The API will expose endpoints in the `api` app (see [backend/api/urls.py](backend/api/urls.py) and [backend/api/views.py](backend/api/views.py)). The backend loads the ML artifacts and returns model predictions for incoming feature payloads.

4) Capture & send features to backend

```bash
python data_capture/main.py
```

- `main.py` coordinates packet capture, flow building, and sending features. Alternatively, run individual modules under `data_capture/capture/` and use the sender at `data_capture/sender/send_to_backend.py` to POST to the backend.

Example POST shape expected by the backend (approximate):

```json
{
  "features": [0.12, 1024, 1, ...]  
}
```

Refer to `backend/api/serializers.py` for the exact input schema.

---

## ML Preprocessing Compatibility

- The training pipeline in `ml/train.py` applies:
  - Column dropping (helper `utils.preprocessing.drop_unused_columns`)
  - Categorical encoding (`utils.preprocessing.encode_categorical`)
  - Standard scaling (`sklearn.preprocessing.StandardScaler` saved to `ml/models/scaler.pkl`)

- The data capture and backend preprocessing must apply the same column selection, encoding mapping, and scaling in the same order and with the same saved `encoders.pkl` and `scaler.pkl`. The `ml/` utilities save `encoders.pkl` and `scaler.pkl` for this reason.

---

## Configuration & Paths

- Training config is defined at the top of `ml/train.py` (DATA_PATH, SCALER_PATH, MODEL_PATH).
- Backend settings for model paths should point to the artifacts saved by training (update `backend/netsense/settings.py` or `backend/api/feature_config.py` if present).

---

## Troubleshooting

- If the backend fails to load model artifacts: verify `ml/models/lstm_autoencoder.h5`, `ml/models/scaler.pkl`, and `ml/models/encoders.pkl` exist and paths in the backend settings are correct.
- If captured features produce mismatched shapes: confirm `data_capture` feature builder uses the same column order and categorical encodings as the training pipeline.
- For model training GPU issues: ensure appropriate TensorFlow version is installed and CUDA/cuDNN are configured on your system.

---

## Tests

- There is an initial `backend/api/tests.py` file for unit tests; run Django tests with:

```bash
cd backend
python manage.py test
```

---

## Contributing

- Keep preprocessing consistent. When adding features, update `ml/utils/preprocessing.py`, retrain the model, and update `ml/models/encoders.pkl` and `ml/models/scaler.pkl` used by the backend.
- Open issues and pull requests for bugs or feature additions.

---

## License

Specify your license here (e.g., MIT) or add a `LICENSE` file.

---

If you'd like, I can also:
- Run a local training pass and report output logs.
- Start the backend and run a sample prediction using `ml/inference.py`.

Last updated: automatic README generated by an assistant.
