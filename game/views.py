import random
from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

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

def game_list(request):
    #Game 객체 전부 가져오기
    games = Game.objects.all()

    ctx = {'games':games}
    return render(request, 'game/game_list.html', ctx)  

def detail(request, pk):
    # post = Post.objects.get(id=pk)
    # user = post.user
    game = Game.objects.get(id=pk)
    attacker = game.attacker
    defender = game.defender

    ctx ={'game':game, 'attacker': attacker, 'defender':defender}
    return render(request, 'game/game_detail.html', ctx)
