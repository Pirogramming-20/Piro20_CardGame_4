import random
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Game, User

class AttackForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["attacker_card", "defender"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AttackForm, self).__init__(*args, **kwargs)
        self.shuffleChoices()

    def shuffleChoices(self):
        if self.request:
            random_numbers = sorted(random.sample(range(1, 11), 5))
            choices = [(str(num), str(num)) for num in random_numbers]
            self.fields['attacker_card'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect,  label="Attacker Card")


    defender = forms.ModelChoiceField(queryset=User.objects.all(), label="Defender")



class CounterForm(forms.ModelForm):
    class Meta:
        model=Game
        fields=['defender_card']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CounterForm, self).__init__(*args, **kwargs)
        self.shuffleChoices()

    def shuffleChoices(self):
        if self.request:
            random_numbers = sorted(random.sample(range(1, 11), 5))
            choices = [(str(num), str(num)) for num in random_numbers]
            self.fields['defender_card'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect,  label="defender Card")
