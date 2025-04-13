from django.urls import path
from .views import*


urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category_list, name='category_list'),
    path('article/<int:id>/', cars_detail, name='cars_detail'),
]
