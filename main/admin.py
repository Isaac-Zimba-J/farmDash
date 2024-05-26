from django.contrib import admin
from .models import SensorData, FlaggedMessage, Animal

# Register your models here.
admin.site.register(SensorData)
admin.site.register(FlaggedMessage)
admin.site.register(Animal)