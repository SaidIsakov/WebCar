from django.urls import path
from .views import*

urlpatterns = [
    path('news/', news, name='news'),
    path('add_form/', add_form, name='add_form')
]
