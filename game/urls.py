from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
    path('main/', main, name='main'),
    path('game_create/', game_create, name='game_create'),
]