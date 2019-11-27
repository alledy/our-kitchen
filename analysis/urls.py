from django.contrib import admin
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    # path('<int:kitchen_info_id>/radius/', views.radius, name='radius'),
    path('<str:lat>/<str:lng>/', views.radius, name='radius'),
    # path('', views.storechart, name = 'storechart'),
    path('', views.kitchen_map, name='kitchen_map'),
    path('2/', views.kitchen_map2, name='kitchen_map2'),
    # path('radius/', views.radius, name= 'radius'),
]
