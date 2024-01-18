import random
from django.shortcuts import render, redirect
from .forms import GameForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            print(game.defender)
            if(game.defender != None and game.defender != request.user):
                game.attacker = request.user
                game.rule = random.randint(0, 1)
                game.save()
                return redirect('/') # 추후 detail 이동으로 수정
    else:
        form = GameForm()
    return render(request, 'game/game_create.html', {'form': form})
            
