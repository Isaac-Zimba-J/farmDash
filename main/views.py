from django.shortcuts import render
import pyrebase
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
SOME_HIGH_CONDUCTIVITY_LEVEL = 1000800.0  # Example high level for conductivity

def index(request):
    # Fetch data from Firestore
    volume = db.child("Data").child("Volume").get().val()
    conductivity = db.child("Data").child("Conductivity").get().val()

    # Initialize flagged_message
    flagged_message = ""

    # Check if data exists and apply logic
    if volume is not None and conductivity is not None:
        if conductivity >= SOME_HIGH_CONDUCTIVITY_LEVEL:
            flagged_message = f"Potential mastisis"



    # Pass data to template
    context = {
        'volume': volume,
        'conductivity': conductivity,
        'flagged_message': flagged_message
    }

    return render(request, 'index.html', context)
