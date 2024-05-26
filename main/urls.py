from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_data/', views.fetch_data, name="fetch_data"),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('view/', views.indexw, name='indexw' ),
]