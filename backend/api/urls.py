from django.urls import path
from .views import NetworkLogListCreate

urlpatterns = [
    path("logs/", NetworkLogListCreate.as_view(), name="network_logs"),
]
