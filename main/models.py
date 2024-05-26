from django.db import models

class SensorData(models.Model):
    volume = models.FloatField()
    conductivity = models.FloatField()
    timestamp = models.DateTimeField()

class FlaggedMessage(models.Model):
    sensor_data = models.ForeignKey(SensorData, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
