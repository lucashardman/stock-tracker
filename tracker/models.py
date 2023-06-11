from os import name
from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
