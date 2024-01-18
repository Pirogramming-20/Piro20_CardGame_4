from django.shortcuts import render
from .models import Game

# Create your views here.
def game_list(request):
    #Game 객체 전부 가져오기
    games = Game.objects.all()

    ctx = {'games':games}
    return render(request, 'game/game_list.html', ctx)