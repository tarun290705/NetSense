from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import AnomalyRecord
from .serializers import NetworkLogSerializer
from .ml_engine import run_inference


class NetworkLogListCreate(ListCreateAPIView):
    queryset = AnomalyRecord.objects.all().order_by("-id")
    serializer_class = NetworkLogSerializer

    def perform_create(self, serializer):
        """
        1. Read raw ML features from request
        2. Run LSTM Autoencoder inference
        3. Convert NumPy values → native Python
        4. Save clean data into DB
        """

        raw_features = self.request.data.get("features")

        if raw_features is None:
            raise ValueError("Missing 'features' field in request body")

        # -------------------------------
        # Run ML inference
        # -------------------------------
        feature_list, mse, anomaly = run_inference(raw_features)

        # -------------------------------
        # FIX: Convert NumPy → Python
        # -------------------------------
        clean_features = [float(x) for x in feature_list]
        clean_mse = float(mse)
        clean_anomaly = bool(anomaly)

        # -------------------------------
        # Save record
        # -------------------------------
        serializer.save(
            features=clean_features,
            reconstruction_error=clean_mse,
            is_anomaly=clean_anomaly
        )
