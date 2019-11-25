from django.db import models
from django.conf import settings

class Kitchen_info(models.Model):
    kitchen_name = models.CharField(max_length=20)
    lat = models.FloatField(blank=False)
    lng = models.FloatField(blank=False)
    image = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField()

class Consulting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kitchen = models.ForeignKey(Kitchen_info, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=False)
    addmission = models.BooleanField(default=False)
