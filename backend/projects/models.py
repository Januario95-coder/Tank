from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, post_save
)

from bottom_plates.models import (
    AllModels, ProbabilityFactorData,
    ConsequenceFactorData, InspectionData,
    Results
)
from selectfields.models import (
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




class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    default_values = models.ForeignKey(
                        to=AllModels,
                        on_delete=models.CASCADE, 
                        blank=True,
                        null=True
                    )

    def __str__(self):
        return self.name
        
   
   
   
@receiver(pre_save, sender=Project)
def project_pre_save(sender, instance, 
                     *args, **kwargs):
    print('Pre-save')
    if instance.default_values is None:
        impresses_cathodic_protect = ImpressCathodicProtection.objects.get(id=1)
        sacrificial_cathodic_propect = SacrificialCathodicPropection.objects.get(id=1)
        bottom_plates_internal_coating_or_linin = BottomPlatesInternalCoatingLining.objects.get(id=1)
        bottom_plates_external_coatin = BottomPlatesExternalCoating.objects.get(id=1)
        storage_condition = StorageConditions.objects.get(id=1)
        types_of_bottom = TypeOfBottom.objects.get(id=1)
        heating_coils_in_tanks = HeatingCoilsInTank.objects.get(id=1)
        products_corrosivity = ProductCorrosivity.objects.get(id=1)
        foundation_types = FoundationType.objects.get(id=1)
        heights_of_foundation = HeightOfFoundation.objects.get(id=1)
        effectiveness_of_drainages = EffectivenessOfDrainage.objects.get(id=1)
        
        probability_factor_data = ProbabilityFactorData.objects.create(
            impresses_cathodic_protect=impresses_cathodic_protect,
            sacrificial_cathodic_propect=sacrificial_cathodic_propect,
            bottom_plates_internal_coating_or_linin=bottom_plates_internal_coating_or_linin,
            bottom_plates_external_coatin=bottom_plates_external_coatin,
            storage_condition=storage_condition,
            types_of_bottom=types_of_bottom,
            heating_coils_in_tanks=heating_coils_in_tanks,
            products_corrosivity=products_corrosivity,
            foundation_types=foundation_types,
            heights_of_foundation=heights_of_foundation,
            effectiveness_of_drainages=effectiveness_of_drainages
        )
        
        
        time_to_repair = TimeToRepair.objects.get(id=1)
        cost_of_repair = CostOfRepair.objects.get(id=1)
        probable_magnitude_of_product_loss = ProbableMagnitudeOfProductLoss.objects.get(id=1)
        likelihood_of_injury_to_personnel = LikelihoodOfInjuryToPersonnel.objects.get(id=1)
        product_flammability_as_per_MCSP = ProductFlammabilityAsPerMCSP.objects.get(id=1)
        product_toxicity = ProductToxicity.objects.get(id=1)
        location_of_tank_farm = LocationOfTankFarm.objects.get(id=1)
        environmetal_hazard_to_soil_and_water_as_the_potential_to_cause = EnvironmetalHazardToSoilAndWater.objects.get(id=1)
        vapour_emission = VapourEmission.objects.get(id=1)
        
        consequence_factor_data = ConsequenceFactorData.objects.create(
            time_to_repair=time_to_repair,
            cost_of_repair=cost_of_repair,
            probable_magnitude_of_product_loss=probable_magnitude_of_product_loss,
            likelihood_of_injury_to_personnel=likelihood_of_injury_to_personnel,
            product_flammability_as_per_MCSP=product_flammability_as_per_MCSP,
            product_toxicity=product_toxicity,
            location_of_tank_farm=location_of_tank_farm,
            environmetal_hazard_to_soil_and_water_as_the_potential_to_cause=environmetal_hazard_to_soil_and_water_as_the_potential_to_cause,
            vapour_emission=vapour_emission
        )
        
        
        acceleration_factor_for_pitting = AccelerationFactorForPitting.objects.get(id=1)
        NDT_method_used_for_thickness_measurements = NDTMethodUsedForThicknessMeasurements.objects.get(id=1)
        frequency_of_internal_inspections_performed_during_service_life = FrequencyOfInternalInspections.objects.get(id=1)
        type_of_interconnecting_bottom_plate_welds_outside_of_annular_section = TypeOfInterconnectingBottomPlateWelds.objects.get(id=1)
        
        inspection_data= InspectionData.objects.create(
            acceleration_factor_for_pitting=acceleration_factor_for_pitting,
            NDT_method_used_for_thickness_measurements=NDT_method_used_for_thickness_measurements,
            frequency_of_internal_inspections_performed_during_service_life=frequency_of_internal_inspections_performed_during_service_life,
            type_of_interconnecting_bottom_plate_welds_outside_of_annular_section=type_of_interconnecting_bottom_plate_welds_outside_of_annular_section
        )
        results = Results.objects.create()
        all_models = AllModels.objects.create(
            probability_factor_data=probability_factor_data,
            consequence_factor_data=consequence_factor_data,
            inspection_data=inspection_data,
            results=results
        )
        instance.default_values = all_models
        print('Setting default values')
    else:
        print('Default values are already set')
    
    
    
@receiver(post_save, sender=Project)
def project_post_save(sender, instance,
                      created,
                      *args, **kwargs):
    if created:
        print(f'{instance} was created')
    else:
        print(f'{instance} was saved')
