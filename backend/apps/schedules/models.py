from django.db import models
from apps.accounts.models import User


class Shift(models.Model):
    worker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shifts')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    approved = models.BooleanField(default=False)
