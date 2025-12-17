from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import AnomalyRecord
from .serializers import NetworkLogSerializer
from .ml_engine import run_inference


class NetworkLogListCreate(ListCreateAPIView):
    queryset = AnomalyRecord.objects.all()
    serializer_class = NetworkLogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract raw ML features
        raw_features = serializer.validated_data.get("features")

        # Run ML inference
        feature_list, mse, is_anomaly = run_inference(raw_features)

        # ----------------------------
        # STORE ONLY IF ANOMALY
        # ----------------------------
        if is_anomaly:
            instance = serializer.save(
                reconstruction_error=mse,
                is_anomaly=True
            )

            response_data = NetworkLogSerializer(instance).data
            response_data["message"] = "⚠️ Anomaly detected and stored"

            return Response(response_data, status=status.HTTP_201_CREATED)

        # ----------------------------
        # NORMAL TRAFFIC → DO NOT STORE
        # ----------------------------
        return Response(
            {
                "message": "✅ Normal traffic detected (not stored)",
                "reconstruction_error": mse,
                "is_anomaly": False
            },
            status=status.HTTP_200_OK
        )
