from levelupapi.models import game_type
from django.db import models


class Game(models.Model):
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
