from django.db import models

from .forms import User


class DuoData(models.Model):
    user_id = models.IntegerField()
    duo_username = models.CharField(max_length=50)
    duo_password = models.CharField(max_length=50)
    duo_known_words = models.JSONField()
