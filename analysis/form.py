from django import forms
from reservation.models import Kitchen_info, Reservation


def Kitchen_infoForm(forms.ModelForm):
    class Meta:
        model = Kitchen_info
        fields = ['kitchen_name', 'lat', 'lng', 'image', 'capacity', ]
