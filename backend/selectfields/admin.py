from django.contrib import admin

from .models import (
    ImpressCathodicProtection,
    SacrificialCathodicPropection,
    BottomPlatesInternalCoatingLining,
    BottomPlatesExternalCoating,
    StorageConditions,
    TypeOfBottom,
    HeatingCoilsInTank,
    ProductCorrosivity,
    FoundationType,
    HeightOfFoundation,
    EffectivenessOfDrainage,
    TimeToRepair,
    CostOfRepair,
    ProbableMagnitudeOfProductLoss,
    LikelihoodOfInjuryToPersonnel,
    ProductFlammabilityAsPerMCSP,
    ProductToxicity,
    LocationOfTankFarm,
    EnvironmetalHazardToSoilAndWater,
    AccelerationFactorForPitting,
    VapourEmission,
    NDTMethodUsedForThicknessMeasurements,
    FrequencyOfInternalInspections,
    TypeOfInterconnectingBottomPlateWelds,
)



@admin.register(ImpressCathodicProtection)
class ImpressCathodicProtectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(SacrificialCathodicPropection)
class SacrificialCathodicPropectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(BottomPlatesInternalCoatingLining)
class BottomPlatesInternalCoatingLiningAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(BottomPlatesExternalCoating)
class BottomPlatesExternalCoatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(StorageConditions)
class StorageConditionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(TypeOfBottom)
class TypeOfBottomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(HeatingCoilsInTank)
class HeatingCoilsInTankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(ProductCorrosivity)
class ProductCorrosivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(FoundationType)
class FoundationTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(HeightOfFoundation)
class HeightOfFoundationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(EffectivenessOfDrainage)
class EffectivenessOfDrainageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(TimeToRepair)
class TimeToRepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(CostOfRepair)
class CostOfRepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(ProbableMagnitudeOfProductLoss)
class ProbableMagnitudeOfProductLossAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(LikelihoodOfInjuryToPersonnel)
class LikelihoodOfInjuryToPersonnelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(ProductFlammabilityAsPerMCSP)
class ProductFlammabilityAsPerMCSPAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(ProductToxicity)
class ProductToxicityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(LocationOfTankFarm)
class LocationOfTankFarmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(EnvironmetalHazardToSoilAndWater)
class EnvironmetalHazardToSoilAndWaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(AccelerationFactorForPitting)
class AccelerationFactorForPittingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(VapourEmission)
class VapourEmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(NDTMethodUsedForThicknessMeasurements)
class NDTMethodUsedForThicknessMeasurementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(FrequencyOfInternalInspections)
class FrequencyOfInternalInspectionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(TypeOfInterconnectingBottomPlateWelds)
class TypeOfInterconnectingBottomPlateWeldsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    