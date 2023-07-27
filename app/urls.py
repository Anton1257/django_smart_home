from django.urls import path
from . import views

urlpatterns = [
    path("sensors/", views.SensorListCreateView.as_view(), name="sensor-list"),
    path(
        "sensors/<int:pk>/",
        views.SensorRetrieveUpdateDeleteView.as_view(),
        name="sensor-retrieve-update-delete",
    ),
    path(
        "measurements/",
        views.TemperatureMeasurementCreateView.as_view(),
        name="measurement-create",
    ),
]
