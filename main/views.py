from django.shortcuts import render
import pyrebase
from django.utils import timezone
from .models import SensorData, FlaggedMessage, Animal
from datetime import datetime


from django.http import JsonResponse


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
SOME_HIGH_CONDUCTIVITY_LEVEL = 10.0  # Example high level for conductivity

def index(request):
    # Fetch data from Firestore
  
    volume_data = SensorData.objects.latest('volume')
    conductivity_data =SensorData.objects.latest('conductivity')
    timestamp_data = SensorData.objects.latest('timestamp')

    volume = volume_data.volume
    conductivity = conductivity_data.conductivity
    timestamp = timestamp_data.timestamp

    flagged_message = ""

    # show animal data
    animal_data = Animal.objects.all()

 
    if volume is not None and conductivity is not None:
        data = SensorData(
            volume = volume,
            conductivity = conductivity,
            timestamp = timestamp
        )
        # ÷data.save()

        # Check conductivity level and create flagged message if needed
        if conductivity >= SOME_HIGH_CONDUCTIVITY_LEVEL:
            flagged_message = f"Potential mastitis6"
            flagged = FlaggedMessage(
                sensor_data=data,
                message=flagged_message,
                timestamp=timezone.now()
            )
            # flagged.save()

    context = {
        "animal_data": animal_data,
    }
    return render(request, 'index.html',context)



def fetch_data(request):
    # Fetch data from the database or wherever it's stored
    # Example: Get the latest SensorData and FlaggedMessage
    latest_data = SensorData.objects.latest('timestamp')
    flagged_message = FlaggedMessage.objects.filter(sensor_data=latest_data).first()

    # Prepare the data to be sent back to the client
    data = {
        'volume': latest_data.volume,
        'conductivity': latest_data.conductivity,
        'flagged_message': flagged_message.message if flagged_message else ''
    }

    return JsonResponse(data)



def add_animal(request):
    if request.method == 'POST':
        animal_id = request.POST.get('animal_id')

        if animal_id:
            animal = Animal(animal_id=animal_id, timestamp=timezone.now())
            animal.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return JsonResponse({'success': False})


def indexw(request):
    return render(request, 'indexw.html')