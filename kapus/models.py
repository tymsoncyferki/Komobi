from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import datetime




class Issue(models.Model):
    title = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=100, default="Transport")
    time = models.DateTimeField(auto_now_add=True, blank=True)
    photo = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=100, default="Przyjęte")
    description = models.TextField(default="")
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title

    status_options = ['Przyjęte', 'W trakcie realizacji', 'Zakończone', 'Odrzucone']
