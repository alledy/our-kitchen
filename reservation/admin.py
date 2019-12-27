from django.contrib import admin
from .models import Kitchen_info, Reservation


class Reservation_Admin(admin.ModelAdmin):
    list_display = ('pk', 'start_date', 'end_date', 'time')


admin.site.register(Reservation, Reservation_Admin)
