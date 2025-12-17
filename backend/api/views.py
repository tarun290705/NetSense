from rest_framework.generics import ListCreateAPIView
from .models import AnomalyRecord
from .serializers import NetworkLogSerializer
from .ml_engine import run_inference

class NetworkLogListCreate(ListCreateAPIView):
    queryset = AnomalyRecord.objects.all()
    serializer_class = NetworkLogSerializer

    def perform_create(self, serializer):
        raw_features = self.request.data.get("features", {})

        features_dict, mse, anomaly = run_inference(raw_features)

        serializer.save(
            features=features_dict,
            reconstruction_error=mse,
            is_anomaly=anomaly
        )
