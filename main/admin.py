from django.contrib import admin
from .models import SensorData, FlaggedMessage, Animal

# Register your models here.
admin.site.register(SensorData)
admin.site.register(FlaggedMessage)
admin.site.register(Animal)

admin.site.site_header = "Farm Management"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"