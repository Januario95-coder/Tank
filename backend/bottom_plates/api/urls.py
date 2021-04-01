from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from .api_views import (
    ProbabilityFactorDataView,
    ConsequenceFactorView,
    InspectionDataView
)


router = DefaultRouter()
router.register('proba-factor', ProbabilityFactorDataView, basename='ProbabilityFactorData')
router.register('conseq-factor', ConsequenceFactorView, basename='ConsequenceFactor')
router.register('inspe-data', InspectionDataView, basename='InspectionData')


urlpatterns = [
    path('', include(router.urls)),
]