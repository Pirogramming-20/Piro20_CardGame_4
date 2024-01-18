from django.db import models
from common.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Game(models.Model):
    rule = models.BooleanField()
    attacker_card = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    defender_card = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], null=True, blank=True)
    attacker=models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='attack_game')
    defender=models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='defend_game')