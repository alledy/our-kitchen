from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('mypage/',views.mypage,name='mypage'),
    path('chat/', views.chat, name='chat'),
    path('webhook/',views.webhook,name='webhook'),
]