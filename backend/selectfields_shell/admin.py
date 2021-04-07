from django.contrib import admin

from .models import (
    impressedCoatingAppliedToSheelPlates,
    ExternalCoatingAppliedToShellPlates,
    StorageConditions,
    HeatedCoilsInTank,
    ProductCorrosivity,
    VaporCorrosivity,
    TankShellHasBeenInsulated,
)



@admin.register(impressedCoatingAppliedToSheelPlates)
class impressedCoatingAppliedToSheelPlatesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(ExternalCoatingAppliedToShellPlates)
class ExternalCoatingAppliedToShellPlatesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(StorageConditions)
class StorageConditionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(HeatedCoilsInTank)
class HeatedCoilsInTankAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(ProductCorrosivity)
class ProductCorrosivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(VaporCorrosivity)
class VaporCorrosivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
@admin.register(TankShellHasBeenInsulated)
class TankShellHasBeenInsulatedAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
  













  
# @admin.register(ProductCorrosivity)
# class ProductCorrosivityAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']


# @admin.register(FoundationType)
# class FoundationTypeAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(HeightOfFoundation)
# class HeightOfFoundationAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(EffectivenessOfDrainage)
# class EffectivenessOfDrainageAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(TimeToRepair)
# class TimeToRepairAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(CostOfRepair)
# class CostOfRepairAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(ProbableMagnitudeOfProductLoss)
# class ProbableMagnitudeOfProductLossAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(LikelihoodOfInjuryToPersonnel)
# class LikelihoodOfInjuryToPersonnelAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(ProductFlammabilityAsPerMCSP)
# class ProductFlammabilityAsPerMCSPAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(ProductToxicity)
# class ProductToxicityAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(LocationOfTankFarm)
# class LocationOfTankFarmAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(EnvironmetalHazardToSoilAndWater)
# class EnvironmetalHazardToSoilAndWaterAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(AccelerationFactorForPitting)
# class AccelerationFactorForPittingAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(VapourEmission)
# class VapourEmissionAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(NDTMethodUsedForThicknessMeasurements)
# class NDTMethodUsedForThicknessMeasurementsAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(FrequencyOfInternalInspections)
# class FrequencyOfInternalInspectionsAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    
# @admin.register(TypeOfInterconnectingBottomPlateWelds)
# class TypeOfInterconnectingBottomPlateWeldsAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name']
    
    