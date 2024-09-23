from django.shortcuts import render
import pyrebase
from django.utils import timezone
from .models import SensorData, FlaggedMessage, Animal
from datetime import datetime


from django.http import JsonResponse


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
SOME_HIGH_CONDUCTIVITY_LEVEL = 6  # Example high level for conductivity

def index(request):
    # Fetch data from Firestore
  
    volume_data = SensorData.objects.latest('volume')
    conductivity_data =SensorData.objects.latest('conductivity')
    timestamp_data = SensorData.objects.latest('timestamp')

    volume = db.child("Flow_Sensor").child("Flow sensor:").get().val()
    conductivity = db.child("Electrical Conductivity").child("Conductivity").get().val()
    timestamp = timestamp_data.timestamp

    flagged_message = ""

    # show animal data
    animal_data = Animal.objects.all()


        # Determine flagged message based on conductivity
    if conductivity is not None:
        if conductivity >= SOME_HIGH_CONDUCTIVITY_LEVEL:
            flagged_message = "Potential mastitis"
        else:
            flagged_message = "All good"
    else:
        flagged_message = "No data available"
    # if volume is not None and conductivity is not None:
    #     data = SensorData(
    #         volume = volume,
    #         conductivity = conductivity,
    #         timestamp = timestamp
    #     )
    #     # ÷data.save()

    #     # Check conductivity level and create flagged message if needed
    #     if conductivity_data.conductivity >= SOME_HIGH_CONDUCTIVITY_LEVEL:
    #         flagged_message = f"Potential mastitis"
    #         flagged = FlaggedMessage(
    #             sensor_data=data,
    #             message=flagged_message,
    #             timestamp=timezone.now()
    #         )
    #         # flagged.save()

    context = {
        "animal_data": animal_data,
        "volume": volume,
        "conductivity": conductivity,
        "timestamp": timestamp,
        "flagged_message": flagged_message,
        
    }
    return render(request, 'index.html',context)





def fetch_data(request):
    latest_sensor_data = SensorData.objects.order_by('-timestamp').first()
    
    if not latest_sensor_data:
        return JsonResponse({
            'volume': 0,
            'conductivity': 0,
            'timestamp': None,
            'flagged_message': 'No data available',
        })
    
    flagged_message = FlaggedMessage.objects.filter(sensor_data=latest_sensor_data).first()

    data = {
        'volume': latest_sensor_data.volume,
        'conductivity': latest_sensor_data.conductivity,
        'timestamp': latest_sensor_data.timestamp,
        'flagged_message': flagged_message.message if flagged_message else 'No flagged message',
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





def get_animal_data(request):
    # Replace with your actual logic to fetch the animal data
    animal_data = [
        {
            'volume': db.child("Flow_Sensor").child("Flow sensor:").get().val(),    # Example updated value
            'conductivity': db.child("Electrical Conductivity").child("Conductivity").get().val()  # Example updated value
        }
    ]
    return JsonResponse(animal_data, safe=False)