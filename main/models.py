from django.db import models

class SensorData(models.Model):
    volume = models.FloatField()
    conductivity = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Volume : {self.volume} Conductivity : {self.conductivity} Timestamp : {self.timestamp}"
class FlaggedMessage(models.Model):
    sensor_data = models.ForeignKey(SensorData, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.message}"

class Animal(models.Model):
    animal_id = models.CharField(max_length=100, unique=True)
    volume = models.FloatField(default=45.0)
    conductivity = models.FloatField(default=45.0)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.animal_id