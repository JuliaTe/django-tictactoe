from django.shortcuts import render
from gameplay.models import Game

# Create your views here.

def home(request):
  my_game = Game.objects.games_for_user(request.user)
  active_games = my_game.active()

  return render(request, "player/home.html",
               { 'games': active_games})

