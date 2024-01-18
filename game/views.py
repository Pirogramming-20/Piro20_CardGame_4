from django.shortcuts import render
from .forms import GameForm

def main(request):
    return render(request, template_name='game/main.html')

def game_create(request):
    form = GameForm()
    ctx = {'form': form}
    return render(request, template_name='game/game_create.html', context=ctx)