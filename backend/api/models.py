from django.db import models

class AnomalyRecord(models.Model):
    src_ip = models.CharField(max_length=200, null=True, blank=True)
    dst_ip = models.CharField(max_length=200, null=True, blank=True)
    protocol = models.CharField(max_length=50)  # numeric protocol stored as string
    length = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    features = models.JSONField(null=True, blank=True)
    reconstruction_error = models.FloatField(null=True, blank=True)
    is_anomaly = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.src_ip} -> {self.dst_ip} | Anomaly: {self.is_anomaly}"
