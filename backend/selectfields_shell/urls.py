from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    impressedCoatingAppliedToSheelPlatesView,
    ExternalCoatingAppliedToShellPlatesView,
    StorageConditionsView,
    HeatedCoilsInTankView,
    ProductCorrosivityView,
    VaporCorrosivityView,
    TankShellHasBeenInsulatedView,
)


router = DefaultRouter()
router.register('impress-cathodic', impressedCoatingAppliedToSheelPlatesView, basename='impressedCoatingAppliedToSheelPlates')
router.register('sacrificial-cathodic', ExternalCoatingAppliedToShellPlatesView, basename='ExternalCoatingAppliedToShellPlates')
router.register('storage-conditions', StorageConditionsView, basename='StorageConditions')
router.register('internal-coating', HeatedCoilsInTankView, basename='HeatedCoilsInTank')
router.register('external-coating', ProductCorrosivityView, basename='ProductCorrosivity')
router.register('type-of-bottom', VaporCorrosivityView, basename='VaporCorrosivity')
router.register('heating-coils', TankShellHasBeenInsulatedView, basename='TankShellHasBeenInsulated')



urlpatterns = [
    path('', include(router.urls))
]