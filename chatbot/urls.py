from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('webhook/',views.webhook,name='webhook'),
]