from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reserve'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:kitchen_pk>/', views.MonthCalendar.as_view(), name="reservation"),
    path('<int:kitchen_pk>/<int:year>/<int:month>/',
         views.MonthCalendar.as_view(), name="reservation"),
]
