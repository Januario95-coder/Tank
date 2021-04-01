
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProjectView,
    delete_project,
    get_user,
    create_project,
    update_project,
    update_project_details
)

router = DefaultRouter()
router.register('projects', ProjectView, basename='Project')


urlpatterns = [
    path('', include(router.urls)),
    path('projects/delete/', delete_project),
    path('create-project/', create_project),
    path('update-project/', update_project),
    path('update-project-details/', update_project_details),
    path('user/', get_user),
]