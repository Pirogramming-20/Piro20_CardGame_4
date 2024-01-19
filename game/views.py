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
    games = Game.objects.filter(Q(attacker=user) | Q(defender=user)).order_by('-created_date')
    ctx = {'games':games}
    return render(request, 'game/game_list.html', ctx)

def detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    userState, userScore = checkWinner(game, request.user)
    ctx ={'game': game, 'result':userState, 'score': userScore}
    return render(request, 'game/game_detail.html', ctx)

def detail_ing(request,pk):
    game = get_object_or_404(Game, pk=pk)
    attacker = game.attacker
    defender = game.defender

    ctx ={'game':game, 'attacker': attacker, 'defender':defender}
    return render(request, 'game/game_detail_ing.html', ctx)

def ranking(request):
    user_list = User.objects.order_by('-user_score')
    if len(user_list) >= 3:
        user_list = user_list[:3]
    return render(request, 'game/game_ranking.html', {'user_list': user_list})

def checkWinner(game, user):
    userState, userScore = 2, 0
    if game.rule == True: #Bigger card win
        if game.attacker_card > game.defender_card:
            game.attacker.user_score += game.attacker_card
            game.defender.user_score -= game.defender_card
            # 1: User win, 0: User defeat 
            if (game.attacker == user):
                userState, userScore = 1, game.attacker_card
            else:
                userState, userScore = 0, -game.defender_card
        elif game.attacker_card < game.defender_card:
            game.attacker.user_score -= game.attacker_card
            game.defender.user_score += game.defender_card
            if (game.defender == user):
                userState, userScore = 1, game.defender_card
            else:
                userState, userScore = 0, -game.attacker_card
    else: # Smaller card win
        if game.attacker_card > game.defender_card:
            game.attacker.user_score -= game.attacker_card
            game.defender.user_score += game.defender_card
            if (game.defender == user):
                userState, userScore = 1, game.defender_card
            else:
                userState, userScore = 0, -game.attacker_card
        elif game.attacker_card < game.defender_card:
            game.attacker.user_score += game.attacker_card
            game.defender.user_score -= game.defender_card
            if (game.attacker == user):
                userState, userScore = 1, game.attacker_card
            else:
                userState, userScore = 0, -game.defender_card
    game.attacker.save()
    game.defender.save()
    return userState, userScore   
        
def counter(request, pk):
    game = get_object_or_404(Game, id=pk)
    if request.method == 'POST':
        form = CounterForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            userState, userScore = checkWinner(game, request.user)
            return render(request, 'game/game_detail.html', {'game': game, 'result':userState, 'score': userScore})            
    else:
        if game.defender_card != None:
            return redirect('game:game_list')
        form = CounterForm(instance=game)
    return render(request, 'game/game_counter.html', {'form': form, 'pk': pk})

def game_delete(request, pk):
    if request.method == 'POST':
        Game.objects.get(id=pk).delete()
    return redirect('game:game_list')

def detail_defend(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game/game_detail_defend.html', {'game': game})