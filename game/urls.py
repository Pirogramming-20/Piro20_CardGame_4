from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
    path('list/', game_list, name='game_list'),
    path('create/', create, name='create'),
    path('counter/<int:pk>', counter, name='counter'),
    path('detail/<int:pk>/', detail, name='detail'),
]