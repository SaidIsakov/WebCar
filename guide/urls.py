from django.urls import path
from .views import*

urlpatterns = [
    path('guide/', guide, name='guide'),
    
]