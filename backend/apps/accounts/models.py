from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('boss', 'Boss'),
    )
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='worker')
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True)
