from django.db import models

from .forms import User


class DuoData(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    known_words = models.JSONField()
    languages = models.JSONField()
