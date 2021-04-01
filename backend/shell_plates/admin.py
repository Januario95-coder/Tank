from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    ProbabilityFactorData,
    ConsequenceFactorData,
    InspectionData,
    Results
)


@admin.register(ProbabilityFactorData)
class ProbabilityFactorDataAdmin(admin.ModelAdmin):
    list_dislay = ['id', 'impressed_coating_applied_to_sheel_plates',
                    'external_coating_applied_to_shell_plates',
                    
                    'storage_conditions'
                    'heating_coils_in_tank',
                    'product_corrosivity',
                    'vapour_corrosivity', 
                    'corrosion_under_insulation_CUI']



@admin.register(ConsequenceFactorData)
class ConsequenceFactorDataAdmin(admin.ModelAdmin):
    list_dislay = ['id', 'time_to_repair', 'cost_of_repair', 
                   'probable_magnitude_of_product_loss',
                   
                   'likelihood_of_injury_to_personnel',
                   'product_flammability_as_per_MCSP',
                   'product_toxicity',
                   'location_of_tank_farm',
                   'continued_location_of_tank_farm',
                   
                   'environmetal_hazard_to_soil_and_water_as_the_potential_to_cause',
                   'vapour_emission']
                   


@admin.register(InspectionData)
class InspectionDataAdmin(admin.ModelAdmin):
    list_dislay = ['id', 'last_inspection',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_1',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_2',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_3',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_4',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_5',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_6',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_7',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_8',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_9',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_10',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_11',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_12',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_13',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_14',
                   'minimum_thickness_measured_during_previous_inspection_for_shell_plate_15',
                   
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_1',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_2',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_3',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_4',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_5',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_6',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_7',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_8',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_9',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_10',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_11',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_12',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_13',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_14',
                   'minimum_thickness_measured_during_present_inspection_for_shell_plate_14',
                   
                   'minimum_allowable_thickness_for_shell_plate_1',
                   'minimum_allowable_thickness_for_shell_plate_2',
                   'minimum_allowable_thickness_for_shell_plate_3',
                   'minimum_allowable_thickness_for_shell_plate_4',
                   'minimum_allowable_thickness_for_shell_plate_5',
                   'minimum_allowable_thickness_for_shell_plate_6',
                   'minimum_allowable_thickness_for_shell_plate_7',
                   'minimum_allowable_thickness_for_shell_plate_8',
                   'minimum_allowable_thickness_for_shell_plate_9',
                   'minimum_allowable_thickness_for_shell_plate_10',
                   'minimum_allowable_thickness_for_shell_plate_11',
                   'minimum_allowable_thickness_for_shell_plate_12',
                   'minimum_allowable_thickness_for_shell_plate_13',
                   'minimum_allowable_thickness_for_shell_plate_14',
                   'minimum_allowable_thickness_for_shell_plate_15',
                   
                   'estimated_corrosion_for_shell_plate_1',
                   'estimated_corrosion_for_shell_plate_2',
                   'estimated_corrosion_for_shell_plate_3',
                   'estimated_corrosion_for_shell_plate_4',
                   'estimated_corrosion_for_shell_plate_5',
                   'estimated_corrosion_for_shell_plate_6',
                   'estimated_corrosion_for_shell_plate_7',
                   'estimated_corrosion_for_shell_plate_8',
                   'estimated_corrosion_for_shell_plate_9',
                   'estimated_corrosion_for_shell_plate_10',
                   'estimated_corrosion_for_shell_plate_11',
                   'estimated_corrosion_for_shell_plate_12',
                   'estimated_corrosion_for_shell_plate_13',
                   'estimated_corrosion_for_shell_plate_14',
                   'estimated_corrosion_for_shell_plate_15',
                   
                   'NDT_method_used_for_thickness_measurements',
                   'frequency_of_internal_inspections_performed_during_service_life',
                   'corrosion_on_wind_girders',
                   'buckles_in_shell_plates',
                   'differential_setllement_between_tank_structure_and_piping_support'
                   ]
                   
                   
                   
                   
@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_dislay = ['id', 'probability_factor',
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
                   
                   'critical_shell_place',
                   'corrosion_rate',
                   'acceleration_factor_for_pitting',
                   'adjusted_corrosion_rate',
                   'remaining_life',
                   'confidence_factor',
                   'confidence_factor_adjustement',
                   'ajusted_confidence_factor',
                   'interval_before_next_required_inspection',
                   'next_inspection']
                   
                   

        
        
#admin.site.unregister(Group)