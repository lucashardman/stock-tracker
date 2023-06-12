from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    max_val = models.DecimalField(max_digits=10, decimal_places=2)
    min_val = models.DecimalField(max_digits=10, decimal_places=2)
    timmer = models.IntegerField()
    track_time = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    id = models.UUIDField(primary_key=True)
    user = models.CharField(max_length=255) # models.ForeignKey(User, on_delete=models.CASCADE)
    created_at_dt = models.DateTimeField()
    last_check_at_dt = models.DateTimeField()

    def __str__(self):
        return self.name
