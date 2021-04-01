from django.db import models

from .INPUT_FIELDS_SELECTION import *


class ProbabilityFactorData(models.Model):   
    #Action Taken to Limit Corrosion on Bottom Plates
    impressed_coating_applied_to_sheel_plates = models.CharField(max_length=100,
            choices=IMPRESSED_COATING_APPLIED_TO_SHEEL_PLATES,
            verbose_name='1: Impressed coating applied to sheel plates')
    external_coating_applied_to_shell_plates = models.CharField(max_length=100,
            choices=EXTERNAL_COATING_APPLIED_TO_SHELL_PLATES,
            verbose_name='2: External coating applied to shell plates')
            
            
    #Features That Influences The Failure Mechanism of Bottom Plates
    storage_conditions = models.CharField(max_length=100,
            choices=STORAGE_CONDITIONS,
            verbose_name='3a: Storage conditions')
    heating_coils_in_tank = models.CharField(max_length=100,
            choices=HEATING_COILS_IN_TANK,
            verbose_name='3b: Heating coils in tank')
    product_corrosivity = models.CharField(max_length=100,
            choices=PRODUCT_CORROSIVITY,
            verbose_name='4: product corrosivity')
    vapour_corrosivity = models.CharField(max_length=100,
            choices=VAPOUR_CORROSIVITY,
            verbose_name='5: Vapour Corrosivity')
    corrosion_under_insulation_CUI = models.CharField(max_length=100,
            choices=CORROSION_UNDER_INSULATION_CUI,
            verbose_name='6: Corrosion under insulation (CUI)')
            
            
    class Meta:
        verbose_name = 'Probability Factor Data'
        verbose_name_plural = 'Probability Factor Data'
            
               


class ConsequenceFactorData(models.Model):   
    # Economic Aspects
    time_to_repair = models.CharField(max_length=100,
            choices=TIME_TO_REPAIR,
            verbose_name='7a: Time to repair')
    cost_of_repair = models.CharField(max_length=100,
            choices=COST_OF_REPAIR,
            verbose_name='7b: Cost of repair')
    probable_magnitude_of_product_loss = models.CharField(max_length=100,
            choices=PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS,
            verbose_name='7c: Probable magnitude of product loss')
            
    # Health and Safety Aspects
    likelihood_of_injury_to_personnel = models.CharField(max_length=100,
            choices=LIKELIHOOD_OF_INJURY_TO_PERSONNEL,
            verbose_name='9a: Likelihood of injury to personnel')
    product_flammability_as_per_MCSP = models.CharField(max_length=100,
            choices=PRODUCT_FLAMMABILITY_AS_PER_MCSP,
            verbose_name='9b: Product flammability as per MCSP')
    product_toxicity = models.CharField(max_length=100,
            choices=PRODUCT_TOXICITY,
            verbose_name='9c: Product toxicity')
    location_of_tank_farm = models.CharField(max_length=100,
            choices=LOCATION_OF_TANK_FARM,
            verbose_name='9d: Location of tank farm')
    continued_location_of_tank_farm = models.CharField(max_length=100,
            choices=CONTINUED_LOCATION_OF_TANK_FARM,
            verbose_name='9d-cont\'d: Location of tank farm')
        
            

    # Environmental Aspects
    environmetal_hazard_to_soil_and_water_as_the_potential_to_cause = models.CharField(max_length=100,
            choices=ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE,
            verbose_name='11a: Environmetal hazard to soil and water as the potential to cause')
    vapour_emission = models.CharField(max_length=100,
            choices=VAPOUR_EMISSION,
            verbose_name='11b: Vapour emission')

           
    class Meta:
        verbose_name = 'Consequence Factor Data'
        verbose_name_plural = 'Consequence Factor Data'               
    
    
    
    
    
class InspectionData(models.Model): 
    last_inspection = models.DateField()
  
    minimum_thickness_measured_during_previous_inspection_for_shell_plate_1 = models.CharField(max_length=100,
        verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 1')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_2 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 2')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_3 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 3')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_4 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 4')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_5 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 5')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_6 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 6')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_7 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 7')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_8 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 8')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_9 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 9')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_10 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 10')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_11 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 11')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_12 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 12')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_13 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 13')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_14 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate 14')
    # minimum_thickness_measured_during_previous_inspection_for_shell_plate_15 = models.CharField(max_length=100,
        # verbose_name='18B: Minimum thickness measured during previous inspection for shell plate15')
        
    
    minimum_thickness_measured_during_present_inspection_for_shell_plate_1 = models.CharField(max_length=100,
        verbose_name='18C: Minimum thickness measured during present inspection for shell plate 1')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_2 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 2')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_3 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 3')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_4 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 4')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_5 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 5')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_6 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 6')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_7 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 7')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_8 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 8')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_9 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 9')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_10 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 10')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_11 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 11')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_12 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 12')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_13 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 13')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_14 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 14')
    # minimum_thickness_measured_during_present_inspection_for_shell_plate_15 = models.CharField(max_length=100,
        # verbose_name='18C: Minimum thickness measured during present inspection for shell plate 15')
        
    
    minimum_allowable_thickness_for_shell_plate_1 = models.CharField(max_length=100,
        verbose_name='18D: Minimum allowable thickness for shell plate 1')
    # minimum_allowable_thickness_for_shell_plate_2 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 2')
    # minimum_allowable_thickness_for_shell_plate_3 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 3')
    # minimum_allowable_thickness_for_shell_plate_4 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 4')
    # minimum_allowable_thickness_for_shell_plate_5 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 5')
    # minimum_allowable_thickness_for_shell_plate_6 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 6')
    # minimum_allowable_thickness_for_shell_plate_7 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 7')
    # minimum_allowable_thickness_for_shell_plate_8 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 8')
    # minimum_allowable_thickness_for_shell_plate_9 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 9')
    # minimum_allowable_thickness_for_shell_plate_10 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 10')
    # minimum_allowable_thickness_for_shell_plate_11 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 11')
    # minimum_allowable_thickness_for_shell_plate_12 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 12')
    # minimum_allowable_thickness_for_shell_plate_13 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 13')
    # minimum_allowable_thickness_for_shell_plate_14 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 14')
    # minimum_allowable_thickness_for_shell_plate_15 = models.CharField(max_length=100,
        # verbose_name='18D: Minimum allowable thickness for shell plate 15')
        
        
    estimated_corrosion_for_shell_plate_1 = models.CharField(max_length=100,
        verbose_name='18E: Estimated corrosion for shell plate 1')
    # estimated_corrosion_for_shell_plate_2 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 2')
    # estimated_corrosion_for_shell_plate_3 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 3')
    # estimated_corrosion_for_shell_plate_4 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 4')
    # estimated_corrosion_for_shell_plate_5 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 5')
    # estimated_corrosion_for_shell_plate_6 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 6')
    # estimated_corrosion_for_shell_plate_7 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 7')
    # estimated_corrosion_for_shell_plate_8 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 8')
    # estimated_corrosion_for_shell_plate_9 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 9')
    # estimated_corrosion_for_shell_plate_10 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 10')
    # estimated_corrosion_for_shell_plate_11 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 11')
    # estimated_corrosion_for_shell_plate_12 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 12')
    # estimated_corrosion_for_shell_plate_13 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 13')
    # estimated_corrosion_for_shell_plate_14 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 14')
    # estimated_corrosion_for_shell_plate_15 = models.CharField(max_length=100,
        # verbose_name='18E: Estimated corrosion for shell plate 15')

 
            
            
    # Inspections
    NDT_method_used_for_thickness_measurements = models.CharField(max_length=100,
            choices=NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS,
            verbose_name='24: NDT method used for thickness measurements')
    frequency_of_internal_inspections_performed_during_service_life = models.CharField(max_length=100,
            choices=FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE,
            verbose_name='25: Frequency of internal inspections performed during service life')
    corrosion_on_wind_girders = models.CharField(max_length=100,
            choices=CORROSION_ON_WIND_GIRDERS,
            verbose_name='26: Corrosion on wind girders')
    buckles_in_shell_plates = models.CharField(max_length=100,
            choices=BUCKLES_IN_SHELL_PLATES,
            verbose_name='27: Buckles in shell plates')
    differential_setllement_between_tank_structure_and_piping_support = models.CharField(max_length=100,
            choices=DIFFERENTIAL_SETLLEMENT_BETWEEN_TANK_STRUCTURE_AND_PIPING_SUPPORT,
            verbose_name='28: Differential setllement between tank structure and piping support')

           
    class Meta:
        verbose_name = 'Inspection Data'
        verbose_name_plural = 'Inspection Data' 
        
        
        


class Results(models.Model): 
    # RISK ASSESSMENT
    probability_factor = models.CharField(max_length=50)
    probability_rating = models.CharField(max_length=50)
    economic_aspects_consequence_factor = models.CharField(max_length=50)
    economic_aspects_consequence_rating = models.CharField(max_length=50)
    health_and_safety_aspects_consequence_factor = models.CharField(max_length=50)
    health_and_safety_aspects_consequence_rating = models.CharField(max_length=50)
    environmental_aspects_consequence_factor = models.CharField(max_length=50)
    environmental_aspects_consequence_rating = models.CharField(max_length=50)
    overall_consequence_factor = models.CharField(max_length=50)
    overall_consequence_rating = models.CharField(max_length=50)
    risk_rating = models.CharField(max_length=50)
    
    # REMAINING LIFE AND INSPECTION INTERVAL ASSESSMENT
    critical_shell_place = models.CharField(max_length=50)
    corrosion_rate = models.CharField(max_length=50)
    acceleration_factor_for_pitting = models.CharField(max_length=50)
    adjusted_corrosion_rate = models.CharField(max_length=50)
    remaining_life = models.CharField(max_length=50)
    confidence_factor = models.CharField(max_length=50)
    confidence_factor_adjustement = models.CharField(max_length=50)
    ajusted_confidence_factor = models.CharField(max_length=50)
    interval_before_next_required_inspection = models.CharField(max_length=50)
    next_inspection = models.DateField()
  
            
    class Meta:
        verbose_name = 'Results'
        verbose_name_plural = 'Results' 
        
        
        
