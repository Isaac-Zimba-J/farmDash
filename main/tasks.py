from celery import shared_task 
import pyrebase 
from .models import SensorData, FlaggedMessage
from django.utils import timezone 
from datetime import datetime
import time


# Firebase configuration
firebaseConfig = {
    # "apiKey": "AIzaSyC07PUOYzuKvD3OhC7MDMF8OVH1H_B0lPY",
    # "authDomain": "testfarm-918d8.firebaseapp.com",
    # "databaseURL": "https://testfarm-918d8-default-rtdb.firebaseio.com",
    # "projectId": "testfarm-918d8",
    # "storageBucket": "testfarm-918d8.appspot.com",
    # "messagingSenderId": "213718537578",
    # "appId": "1:213718537578:web:76a9080a611c9028dfc113"

  "apiKey": "AIzaSyAa1gq2hGnEIY9q5zqQDaxytHPuzzLd3Wk",
  "authDomain": "mastisis-system.firebaseapp.com",
  "databaseURL": "https://mastisis-system-default-rtdb.firebaseio.com",
  "projectId": "mastisis-system",
  "storageBucket": "mastisis-system.appspot.com",
  "messagingSenderId": "303939488937",
  "appId": "1:303939488937:web:64b38b5b5980dd70ac6db8",
  "measurementId": "G-NXH2NWE5HM"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# Constants
SOME_HIGH_CONDUCTIVITY_LEVEL = 10  # Example high level for conductivity




@shared_task
def fetch_data_from_firebase():
    # Fetch values from Firebase
    volume = db.child("Flow_Sensor").child("Flow sensor:").get().val()
    conductivity = db.child("Electrical Conductivity").child("Conductivity").get().val()
    timestamp = datetime.now()  # Get the current timestamp

    # Only proceed if volume and conductivity are not None
    if volume is not None and conductivity is not None:
        # Check if the latest entry is the same
        latest_data = SensorData.objects.order_by('-timestamp').first()

        # Only save if the new data is different
        if latest_data is None or (latest_data.volume != volume or latest_data.conductivity != conductivity):
            data = SensorData.objects.create(
                volume=volume,
                conductivity=conductivity,
                timestamp=timezone.now()  # Use timezone-aware timestamp
            )

            # Check for high conductivity and create flagged message if necessary
            if conductivity >= SOME_HIGH_CONDUCTIVITY_LEVEL:
                FlaggedMessage.objects.create(
                    sensor_data=data,
                    message="Potential mastitis",
                    timestamp=timezone.now()  # Use timezone-aware timestamp
                )
