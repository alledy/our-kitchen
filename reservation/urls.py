from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:kitchen_pk>/', views.kitchen_detail, name="kitchen_detail"),
]
