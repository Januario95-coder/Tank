from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bottom-plates/', include('bottom_plates.urls')),
    path('api/v1/tanks/', include('bottom_plates.api.urls')),
    path('api/v1/', include('projects.urls')),
    path('api/v1/selectfields/', include('selectfields.urls')),
    path('api/v1/selectfields/toupdate/', include('selectfields.urls2')),
]
