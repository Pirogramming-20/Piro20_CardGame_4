import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AttackForm, CounterForm
from django.db.models import Q
from .models import Game
from common.models import User
# Create your views here.
def attack(request):
    if request.method == 'POST':
        form = AttackForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            if(game.defender != None and game.defender != request.user):
                game.attacker = request.user
                game.rule = random.randint(0, 1)
                game.save()
                return redirect('/') # 추후 detail 이동으로 수정
    else:
        form = AttackForm()
    return render(request, 'game/game_create.html', {'form': form})

def game_list(request):
    user = request.user
    #Game 객체 전부 가져오기
    games = Game.objects.filter(Q(attacker=user) | Q(defender=user))

    ctx = {'games':games}
    return render(request, 'game/game_list.html', ctx)

def detail(request, pk):
    # post = Post.objects.get(id=pk)
    # user = post.user
    game = get_object_or_404(Game, pk=pk)
    attacker = game.attacker
    defender = game.defender

    ctx ={'game':game, 'attacker': attacker, 'defender':defender}
    return render(request, 'game/game_detail.html', ctx)

def ranking(request):
    user_list = User.objects.order_by('-user_score')
    if len(user_list) >= 3:
        user_list = user_list[:3]
    return render(request, 'game/game_ranking.html', {'user_list': user_list})
def counter(request, pk):
    game = get_object_or_404(Game, id=pk)

    if request.method == 'POST':
        form = CounterForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
    else:
        form = CounterForm(instance=game)

    return render(request, 'game/game_counter.html', {'form': form, 'pk': pk})
