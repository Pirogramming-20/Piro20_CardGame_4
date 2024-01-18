from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
    path('list/', game_list, name='game_list'),
    path('attack/', attack, name='attack'),
    path('counter/<int:pk>', counter, name='counter'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('ranking/', ranking, name='ranking'),
    path('detail_ing/<int:pk>', detail_ing, name='detail_ing'),
    path('delete/<int:pk>', game_delete, name='game_delete')
]