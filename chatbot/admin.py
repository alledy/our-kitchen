from django.contrib import admin
from .models import Kitchen_info, Consulting

class Kitchen_infoAdmin(admin.ModelAdmin):
    list_display = ('pk','kitchen_name','lat','lng','capacity')

admin.site.register(Kitchen_info, Kitchen_infoAdmin)

class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('pk','user','kitchen','datetime','addmission')

admin.site.register(Consulting, ConsultingAdmin)
