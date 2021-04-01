from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ImpressCathodicProtectionView,
    SacrificialCathodicPropectionView,
    BottomPlatesInternalCoatingLiningView,
    BottomPlatesExternalCoatingView,
    StorageConditionsView,
    TypeOfBottomView,
    HeatingCoilsInTankView,
    ProductCorrosivityView,
    FoundationTypeView,
    HeightOfFoundationView,
    EffectivenessOfDrainageView,
    TimeToRepairView,
    CostOfRepairView,
    ProbableMagnitudeOfProductLossView,
    LikelihoodOfInjuryToPersonnelView,
    ProductFlammabilityAsPerMCSPView,
    ProductToxicityView,
    LocationOfTankFarmView,
    EnvironmetalHazardToSoilAndWaterView,
    VapourEmissionView,
    AccelerationFactorForPittingView,
    NDTMethodUsedForThicknessMeasurementsView,
    FrequencyOfInternalInspectionsView,
    TypeOfInterconnectingBottomPlateWeldsView,
)



router = DefaultRouter()
router.register('impress-cathodic', ImpressCathodicProtectionView, basename='ImpressCathodicProtection')
router.register('sacrificial-cathodic', SacrificialCathodicPropectionView, basename='SacrificialCathodicPropection')
router.register('internal-coating', BottomPlatesInternalCoatingLiningView, basename='BottomPlatesInternalCoatingLining')
router.register('external-coating', BottomPlatesExternalCoatingView, basename='BottomPlatesExternalCoating')
router.register('storage-conditions', StorageConditionsView, basename='StorageConditions')
router.register('type-of-bottom', TypeOfBottomView, basename='TypeOfBottom')
router.register('heating-coils', HeatingCoilsInTankView, basename='HeatingCoilsInTank')
router.register('product-corrosivity', ProductCorrosivityView, basename='ProductCorrosivity')
router.register('foundation-type', FoundationTypeView, basename='FoundationType')
router.register('height-of-foundation', HeightOfFoundationView, basename='HeightOfFoundation')
router.register('effectivenessOf-drainage', EffectivenessOfDrainageView, basename='EffectivenessOfDrainage')
router.register('time-to-repair', TimeToRepairView, basename='TimeToRepair')
router.register('cost-of-repair', CostOfRepairView, basename='CostOfRepair')
router.register('drainage-magnitude', ProbableMagnitudeOfProductLossView, basename='ProbableMagnitudeOfProductLoss')
router.register('likelihood-of-injury', LikelihoodOfInjuryToPersonnelView, basename='LikelihoodOfInjuryToPersonnel')
router.register('product-flamability', ProductFlammabilityAsPerMCSPView, basename='ProductFlammabilityAsPerMCSP')
router.register('product-toxicity', ProductToxicityView, basename='ProductToxicity')
router.register('location-of-tank', LocationOfTankFarmView, basename='LocationOfTankFarm')
router.register('environmental-hazard', EnvironmetalHazardToSoilAndWaterView, basename='EnvironmetalHazardToSoilAndWater')
router.register('vapour-emission', VapourEmissionView, basename='VapourEmission')
router.register('accelaration-factor', AccelerationFactorForPittingView, basename='AccelerationFactorForPitting')
router.register('ndt-method-used', NDTMethodUsedForThicknessMeasurementsView, basename='NDTMethodUsedForThicknessMeasurements')
router.register('freq-of-internal-insp', FrequencyOfInternalInspectionsView, basename='FrequencyOfInternalInspections')
router.register('type-of-internecting', TypeOfInterconnectingBottomPlateWeldsView, basename='TypeOfInterconnectingBottomPlateWelds')



urlpatterns = [
    path('', include(router.urls))
]