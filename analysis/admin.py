from django.contrib import admin
from .models import Kitchen_info


class Kitchen_info_Admin(admin.ModelAdmin):
    list_display = ('pk', 'kitchen_name', 'lat', 'lng', 'capacity')

admin.site.register(Kitchen_info, Kitchen_info_Admin)
