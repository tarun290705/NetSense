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

        raw_features = serializer.validated_data.get("features")

        features_dict, mse, is_anomaly, threshold = run_inference(raw_features)

    # =================================================
    # SHOW ALL PACKETS IN TERMINAL
    # =================================================
        print("=" * 60)
        print("📦 PACKET RECEIVED")
        print(f"MSE        : {mse:.6f}")

        if threshold is None:
            print("Threshold  : WARM-UP")
            print("Status     : Learning baseline")
        else:
            print(f"Threshold  : {threshold:.6f}")
            print(f"Anomaly    : {is_anomaly}")

        print("=" * 60)

    # =================================================
    # STORE ONLY TRUE ANOMALIES
    # =================================================
        if threshold is not None and is_anomaly:
            instance = serializer.save(
                reconstruction_error=mse,
                is_anomaly=True
            )

            response_data = NetworkLogSerializer(instance).data
            response_data["message"] = "⚠️ Anomaly detected and stored"

            return Response(response_data, status=status.HTTP_201_CREATED)

    # Normal or warm-up traffic
        return Response(
            {
                "message": "✅ Normal traffic (not stored)",
                "reconstruction_error": mse,
                "threshold": threshold,
                "is_anomaly": False
            },
            status=status.HTTP_200_OK
        )
