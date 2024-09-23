from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    
    path('add_animal/', views.add_animal, name='add_animal'),
    path('view/', views.indexw, name='indexw' ),
    path('animal-data/', views.get_animal_data, name='animal-data'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
]