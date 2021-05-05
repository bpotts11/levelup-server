from levelupapi.models import gamer, event
from django.db import models


class EventGamer(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    Event = models.ForeignKey("Event", on_delete=models.CASCADE)
