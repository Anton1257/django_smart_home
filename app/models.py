from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class TemperatureMeasurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, related_name="measurements", on_delete=models.CASCADE
    )
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Measurement for {self.sensor}: {self.temperature} C at {self.created_at}"
        )
