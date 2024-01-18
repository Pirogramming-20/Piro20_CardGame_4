from django import forms
from .models import Game

class AttackForm(forms.ModelForm):
    class Meta:
        model=Game
        fields=["attacker_card", "defender"]

class DefendForm(forms.ModelForm):
    class Meta:
        model=Game
        fields=["defender_card"]
