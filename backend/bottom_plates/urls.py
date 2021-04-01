from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProbabilityFactorDataView,
    ConsequenceFactorDataView,
)

# router = DefaultRouter()
# router.register('probability', ProbabilityFactorDataView)
# router.register('conseq-factor', ConsequenceFactorDataView)


urlpatterns = [
    #path('', include(router.urls)),
    
    path('probability/', ProbabilityFactorDataView.as_view()),
    path('conseq-factor/', ConsequenceFactorDataView.as_view()),
]