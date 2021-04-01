from django.contrib import admin

from .models import (
    ProbabilityFactorData,
    ConsequenceFactorData,
    InspectionData,
    Results, 
)


@admin.register(ProbabilityFactorData)
class ProbabilityFactorDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'impresses_cathodic_protect',
                    'sacrificial_cathodic_propect',
                    'bottom_plates_internal_coating_or_linin',
                    'bottom_plates_external_coatin',
                    
                    'storage_condition',
                    'types_of_bottom',
                    'heating_coils_in_tanks',
                    'products_corrosivity', 
                    
                    'foundation_types',
                    'heights_of_foundation',
                    'effectiveness_of_drainages']
    list_per_page = 12



@admin.register(ConsequenceFactorData)
class ConsequenceFactorDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_to_repair', 'cost_of_repair', 
                   'probable_magnitude_of_product_loss',
                   
                   'likelihood_of_injury_to_personnel',
                   'product_flammability_as_per_MCSP',
                   'product_toxicity',
                   'location_of_tank_farm',
                   
                   'environmetal_hazard_to_soil_and_water_as_the_potential_to_cause',
                   'vapour_emission']
    list_per_page = 12
                   


@admin.register(InspectionData)
class InspectionDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_inspection',
                   'minimum_thickness_measured_during_previous_inspection',
                   'period_of_service_between_previous_inspection_and_this_inspection',
                   'minimum_thickness_measured_during_present_inspection',
                   'minimum_allowable_bottom_place_thickness',
                   'acceleration_factor_for_pitting',
                   
                   'NDT_method_used_for_thickness_measurements',
                   'frequency_of_internal_inspections_performed_during_service_life',
                   'type_of_interconnecting_bottom_plate_welds_outside_of_annular_section']
    list_per_page = 12
                   
                   
                   
                   
@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'probability_factor',
                   'probability_rating', 
                   'economic_aspects_consequence_factor',
                   'economic_aspects_consequence_rating',
                   'health_and_safety_aspects_consequence_factor',
                   'health_and_safety_aspects_consequence_rating',
                   'environmental_aspects_consequence_factor',
                   'environmental_aspects_consequence_rating',
                   'overall_consequence_factor',
                   'overall_consequence_rating',
                   'risk_rating',
                   
                   'corrosion_rate',
                   'acceleration_factor_for_pitting',
                   'adjusted_corrosion_rate',
                   'remaining_life',
                   'confidence_factor',
                   'confidence_factor_adjustement',
                   'ajusted_confidence_factor',
                   'interval_before_next_required_inspection',
                   'next_inspection']
    list_per_page = 12
                   
                   
