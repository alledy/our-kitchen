from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """Reservation 모델폼"""

    class Meta:
        model = Reservation
        fields = ('start_date', 'end_date', 'time')
        TIME_CHOICES = (
            ('M', '오전(6시~12시)'),
            ('A', '오후(12시~18시)'),
            ('N', '밤/심야(18시~24시)'),
        )
        widgets = {
            'time': forms.Select(choices=TIME_CHOICES, attrs={
                'class': 'form-control',
            }),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': '날짜를 선택하세요', 'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': '날짜를 선택하세요', 'type': 'date'}),
        }

    def __init__(self, kitchen_pk, *args, **kwargs):
        self.kitchen_pk = kitchen_pk
        super(ReservationForm, self).__init__(*args, **kwargs)

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
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        time = self.cleaned_data['time']
        events = Reservation.objects.filter(kitchen__pk=self.kitchen_pk)
        if events.exists():
            for event in events:
                if self.check_overlap_time(event.time, time):
                    if self.check_overlap_date(event.start_date, event.end_date, start_date, end_date):
                        raise forms.ValidationError("다른 예약과 시간이 겹칩니다: " + str(
                            event.start_date) + ' - ' + str(event.end_date) + ' ' + str(event.get_time_display()))
