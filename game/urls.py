from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
    path('list/', game_list, name='game_list'),
]