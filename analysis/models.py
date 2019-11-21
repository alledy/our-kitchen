from django.db import models

class Kitchen_info(models.Model):
    kitchen_name = models.CharField(max_length=20)
    lat = models.FloatField(blank=False)
    lng = models.FloatField(blank=False)
    image = models.ImageField(blank=True)
    capacity = models.IntegerField()

# class User(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Reservation_time(models.Model):
    kitchen_name = models.ForeignKey(Kitchen_info, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    last_date = models.DateField()
    time = models.IntegerField()

    

    


     