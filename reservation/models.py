from django.db import models
from django.core.exceptions import ValidationError

# 나중에 analysis앱에서 임포트할 예정


class Kitchen_info(models.Model):
    kitchen_name = models.CharField(max_length=20)
    lat = models.FloatField(blank=False)
    lng = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    capacity = models.IntegerField(default=6)

    def __str__(self):
        return f'{self.kitchen_name}의 수용 가능 인원 : {self.capacity}'

# class User(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)

# 일단 로그인 기능 없이 예약 진행
# last_date -> end_date
# kitchen_name -> kitchen
# Reservation_time -> Reservation


class Reservation(models.Model):
    kitchen = models.ForeignKey(Kitchen_info, on_delete=models.CASCADE)
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

    # 시간대가 겹치지 않으면 날짜가 겹쳐도 예약 가능
    # 시간대가 겹치면 날짜가 겹치지 않아야 예약 가능
    # existed는 이미 존재하는 예약, new는 추가될 예약

    def check_overlap_date(self, existed_start, existed_end, new_start, new_end):
        overlap = True
        if existed_end < new_start:
            overlap = False
        if new_end < existed_start:
            overlap = False
        return overlap

    def check_overlap_time(self, existed_time, new_time):
        overlap = False
        if existed_time == new_time:
            overlap = True
        return overlap

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("끝나는 날짜가 시작 날짜보다 커야 합니다")

        # if self.kitchen.capacity == 0:
        #     raise ValidationError("현재 해당 지점의 예약이 모두 차있어 예약이 불가합니다.")

        diff = self.end_date - self.start_date
        if diff.days < 90:
            raise ValidationError("예약 기간은 90일 이상이어야 합니다.")

        # events = Reservation.objects.all()
        # if events.exists():
        #     for event in events:
        #         if self.check_overlap_time(event.time, self.time):
        #             if self.check_overlap_date(event.start_date, event.end_date, self.start_date, self.end_date):
        #                 raise ValidationError("다른 예약과 시간이 겹칩니다: " + str(
        #                     event.start_date) + ' - ' + str(event.end_date) + ' ' + str(event.get_time_display()))
