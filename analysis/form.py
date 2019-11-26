from django import forms
from .models import Kitchen_info, Reservation_time

def Kitchen_infoForm(forms.ModelForm):
    class Meta:
        model = Kitchen_info
        fields = ['kitchen_name','lat','lng','image','capacity',]

