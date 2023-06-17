from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    link = models.CharField(max_length=10)
    count_sub = models.IntegerField(default=0)

class City(models.Model):
    name = models.CharField(max_length=30)
    weather_data = models.JSONField(default=list)

class Subscriptions(models.Model):
    user_name = models.CharField(max_length=10)
    city_name = models.CharField(max_length=30)
    time = models.TimeField(auto_now=False, auto_now_add=False)