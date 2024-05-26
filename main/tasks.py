from celery import shared_task 
import pyrebase 
from .models import SensorData, FlaggedMessage
from django.utils import timezone 


# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyC07PUOYzuKvD3OhC7MDMF8OVH1H_B0lPY",
    "authDomain": "testfarm-918d8.firebaseapp.com",
    "databaseURL": "https://testfarm-918d8-default-rtdb.firebaseio.com",
    "projectId": "testfarm-918d8",
    "storageBucket": "testfarm-918d8.appspot.com",
    "messagingSenderId": "213718537578",
    "appId": "1:213718537578:web:76a9080a611c9028dfc113"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# Constants
SOME_HIGH_CONDUCTIVITY_LEVEL = 10  # Example high level for conductivity


@shared_task
def fetch_data_from_firebase():
    volume = db.child("Data").child("Volume").get().val()
    conductivity = db.child("Data").child("Conductivity").get().val()
    timestamp = db.child("Data").child("Timestamp").get().val()

    if volume is not None and conductivity is not None:
        timestamp = timezone.now()  # Adjust timestamp handling as necessary
        data = SensorData.objects.create(
            volume=volume,
            conductivity=conductivity,
            timestamp=timestamp
        )

        if conductivity >= SOME_HIGH_CONDUCTIVITY_LEVEL:
            FlaggedMessage.objects.create(
                sensor_data=data,
                message=f"Potential mastisis",
                timestamp=timestamp
            )