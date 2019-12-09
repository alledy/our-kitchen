from django.contrib import admin
from .models import Consulting

class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('pk','user','kitchen','datetime','addmission')

admin.site.register(Consulting, ConsultingAdmin)
