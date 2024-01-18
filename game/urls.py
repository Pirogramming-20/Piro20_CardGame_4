from django.urls import path, include
from .views import create

app_name = 'game'

urlpatterns = [
    path('create/', create, name='create')
]