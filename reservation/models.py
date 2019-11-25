from django.db import models

# 나중에 analysis앱에서 임포트할 예정


class Kitchen_info(models.Model):
    kitchen_name = models.CharField(max_length=20)
    lat = models.FloatField(blank=False)
    lng = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    capacity = models.IntegerField(default=6)

    def __str__(self):
        return f'{self.kitchen_name}의 수용 가능 인원 : {self.capacity}'

# class User(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)

# 일단 로그인 기능 없이 예약 진행
# last_date -> end_date


class Reservation_time(models.Model):
    kitchen_name = models.ForeignKey(Kitchen_info, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    # time은 3 Choices
    # Morning(6~12), Afternoon(12~18), Night(18~24)
    TIME_CHOICES = (
        ('M', '오전(6시~12시)'),
        ('A', '오후(12시~18시)'),
        ('N', '밤/심야(18시~24시)'),
    )
    time = models.CharField(max_length=1, choices=TIME_CHOICES)

    def __str__(self):
        return f"{self.start_date} ~ {self.end_date} : {self.time}"
