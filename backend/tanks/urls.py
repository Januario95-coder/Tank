from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bottom-plates/', include('bottom_plates.urls')),
    path('api/v1/tanks/', include('bottom_plates.api.urls')),
    path('api/v1/', include('projects.urls')),
    path('api/v1/selectfields/', include('selectfields.urls')),
    path('api/v1/selectfields/toupdate/', include('selectfields.urls2')),
    
    path('api/v1/shell/selectfields/', include('selectfields_shell.urls')),
    
    path('', index),
]
