from django.urls import path
from .views import*


urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category_list, name='category_list'),
    path('article/<int:id>/', cars_detail, name='cars_detail'),
    path('history/<int:id>/', cars_history, name='cars_history'),
    path('login/', UserLogin, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', Register, name='registartion')
]
