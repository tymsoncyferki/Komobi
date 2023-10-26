from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import datetime


class Issue(models.Model):
    STATUS_CHOICES = (
        ('open', 'Otwarte'),
        ('closed', 'Zamknięte'),
        ('pending', 'Oczekujące'),
    )
    title = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=100, default="Transport")
    time = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.ImageField(blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="pending")
    description = models.TextField(default="")
    latitude = models.FloatField()
    longitude = models.FloatField()

