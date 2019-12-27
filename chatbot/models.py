from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Consulting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    kitchen = models.CharField(max_length=20)
    datetime = models.CharField(max_length=30)
    addmission = models.BooleanField(default=False)
