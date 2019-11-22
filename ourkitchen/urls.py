from django.contrib import admin
from django.urls import path, include
from . import views

# 프로젝트 단위 urls.py에는 app_name 지정따로 없이 네임스페이스 사용
urlpatterns = [
    path('analysis/',  include('analysis.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('reserve/', include('reservation.urls'))
]
