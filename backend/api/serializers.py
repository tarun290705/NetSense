from rest_framework import serializers
from .models import AnomalyRecord

class NetworkLogSerializer(serializers.ModelSerializer):
    # features = raw ML feature dictionary (JSON incoming)
    features = serializers.JSONField(write_only=True)

    class Meta:
        model = AnomalyRecord
        fields = [
            "src_ip",
            "dst_ip",
            "protocol",
            "length",
            "features",  # ← important
            "reconstruction_error",
            "is_anomaly",
        ]
        read_only_fields = ("reconstruction_error", "is_anomaly")
