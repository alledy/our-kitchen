from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    # path('<int:kitchen_info_id>/radius/', views.radius, name='radius'),
    path('', views.kitchen_map, name= 'kitchen_map'),
    # path('radius/', views.radius, name= 'radius'),
]
