from django.db import models

from .forms import User


class DuoData(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    duo_id = models.IntegerField()
    fullname = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    account_created = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    known_words = models.JSONField()
    translations = models.JSONField()
    languages = models.JSONField()
    lang_abrv = models.JSONField()


class LangAbrv(models.Model):
    abrv = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    nativeName = models.CharField(max_length=50)
