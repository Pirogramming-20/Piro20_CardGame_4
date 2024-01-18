from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
    path('list/', game_list, name='game_list'),
    path('attack/', attack, name='attack'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('ranking/', ranking, name='ranking')
]