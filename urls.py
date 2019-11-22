from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('movies/',include('movies.urls')),
    path('jobs/',include('jobs.urls')),
    path('students/', include('students.urls')),
    path('articles/',include('articles.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)