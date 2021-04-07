from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .INPUT_FIELDS_SELECTION import *
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
    VapourEmission,
    AccelerationFactorForPitting,
    NDTMethodUsedForThicknessMeasurements,
    FrequencyOfInternalInspections,
    TypeOfInterconnectingBottomPlateWelds,
)



def extractScore(score):
    return float(score.split('=')[-1])
  
DEGREE_SIGN = u'\N{DEGREE SIGN}'

class ProbabilityFactorData(models.Model):   
    #Action Taken to Limit Corrosion on Bottom Plates
    # impresses_cathodic_protection = models.CharField(max_length=100,
            # choices=IMPRE_CATHODIC_PROTECTION,
            # default='All readings around the periphery > 0.85 V - Score=0',
            # verbose_name='1: Impressed cathodic protection')
    impresses_cathodic_protect = models.ForeignKey(
            to=ImpressCathodicProtection,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # sacrificial_cathodic_propection = models.CharField(max_length=100,
            # choices=SACRIFICIAL_CATHODIC_PROPECTION,
            # default='Sacrificial CP available and operating - Score=0',
            # verbose_name='2: Sacrificial cathodic protection')
    sacrificial_cathodic_propect = models.ForeignKey(
            to=SacrificialCathodicPropection,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # bottom_plates_internal_coating_or_lining = models.CharField(max_length=100,
            # choices=BOTTOM_PLATES_INTERNAL_COATING_OR_LINING,
            # default='Internal coating applied and quality is sound - Score=0',
            # verbose_name='3: Bottom plates internal coating or lining')
    bottom_plates_internal_coating_or_linin = models.ForeignKey(
            to=BottomPlatesInternalCoatingLining,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # bottom_plates_external_coating = models.CharField(max_length=100,
            # choices=BOTTOM_PLATES_EXTERNAL_COATING,
            # default='External coating applied and quality is sound - Score=0',
            # verbose_name='4: Bottom plates internal coating (other than shop primer)')
    bottom_plates_external_coatin = models.ForeignKey(
            to=BottomPlatesExternalCoating,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    
            
    #Features That Influences The Failure Mechanism of Bottom Plates
    # storage_conditions = models.CharField(max_length=100,
            # choices=STORAGE_CONDITIONS,
            # default=f'Temperature of product < 40{DEGREE_SIGN}C - Score=0',
            # verbose_name='5a: Type of bottom')
    storage_condition = models.ForeignKey(
            to=StorageConditions,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # type_of_bottom = models.CharField(max_length=100,
            # choices=TYPE_OF_BOTTOM,
            # default='Cone up - Score=0',
            # verbose_name='5b: Type of bottom')
    types_of_bottom = models.ForeignKey(
            to=TypeOfBottom,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # heating_coils_in_tank = models.CharField(max_length=100,
            # choices=HEATING_COILS_IN_TANK,
            # default='No heating coil or no contact between heating coil and bottom plates - Score=0',
            # verbose_name='5c: Heating coils in tank')
    heating_coils_in_tanks = models.ForeignKey(
            to=HeatingCoilsInTank,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # product_corrosivity = models.CharField(max_length=100,
            # choices=PRODUCT_CORROSIVITY,
            # default='Group 1/Risk H - Score=2',
            # verbose_name='6: Product Corrosivity')
    products_corrosivity = models.ForeignKey(
            to=ProductCorrosivity,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
            
    @property
    def five_score(self):
        value = ((extractScore(self.storage_condition.name) +
                  extractScore(self.types_of_bottom.name) +
                  extractScore(self.heating_coils_in_tanks.name)) / 2.5)
        return value
            

    #Effectiveness of Drainage To Prevent Water Ingress 
    #Under Bottom Plates
    # foundation_type = models.CharField(max_length=100,
            # choices=FOUNDATION_TYPE,
            # default='Piled concrete raft - Score=0',
            # verbose_name='7: Foundation type')
    foundation_types = models.ForeignKey(
            to=FoundationType,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # height_of_foundation = models.CharField(max_length=100,
            # choices=HEIGHT_OF_FOUNDATION,
            # default='Tank bottom free from contact with water - Score=0',
            # verbose_name='8: Height of foundation')
    heights_of_foundation = models.ForeignKey(
            to=HeightOfFoundation,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
    # effectiveness_of_drainage = models.CharField(max_length=150,
            # choices=EFFECTIVENESS_OF_DRAINAGE,
            # default='Slope of tank pad shoulder allows for adequate drainage away from tank bottom - Score=0',
            # verbose_name='9: Effectiveness of drainage')
    effectiveness_of_drainages = models.ForeignKey(
            to=EffectivenessOfDrainage,
            on_delete=models.CASCADE,
            blank=True,
            null=True
    )
           
           
    class Meta:
        verbose_name = 'Probability Factor Data'
        verbose_name_plural = 'Probability Factor Data'
        
    def __str__(self):
        return 'ProbabilityFactorData instance'
            
               


class ConsequenceFactorData(models.Model):   
    # Economic Aspects
    time_to_repair = models.ForeignKey(
            to=TimeToRepair,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    cost_of_repair = models.ForeignKey(
            to=CostOfRepair,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    probable_magnitude_of_product_loss = models.ForeignKey(
            to=ProbableMagnitudeOfProductLoss,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
           
    @property
    def ten_D_score(self):
        value = max((extractScore(self.time_to_repair.name) +
                     extractScore(self.cost_of_repair.name))/2,
                     extractScore(self.probable_magnitude_of_product_loss.name))
        return value
           
    # Health and Safety Aspects
    likelihood_of_injury_to_personnel = models.ForeignKey(
            to=LikelihoodOfInjuryToPersonnel,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    product_flammability_as_per_MCSP = models.ForeignKey(
            to=ProductFlammabilityAsPerMCSP,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    product_toxicity = models.ForeignKey(
            to=ProductToxicity,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    # product_toxicity = models.CharField(max_length=100,
            # choices=PRODUCT_TOXICITY,
            # default='Non-toxic substances- Score=1',
            # verbose_name='12c: Product toxicity'
    # )
    location_of_tank_farm = models.ForeignKey(
            to=LocationOfTankFarm,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    # continued_location_of_tank_farm = models.CharField(max_length=100,
            # choices=CONTINUED_LOCATION_OF_TANK_FARM,
            # default='4',
            # verbose_name='12d-cont\'d: Location of tank farm')
        
    @property
    def twelve_E(self):
        value = max((extractScore(self.product_flammability_as_per_MCSP.name) +
                     extractScore(self.product_toxicity.name) + extractScore(self.location_of_tank_farm.name))/3,
                     extractScore(self.likelihood_of_injury_to_personnel.name))
        return value
            

    # Environmental Aspects
    environmetal_hazard_to_soil_and_water_as_the_potential_to_cause = models.ForeignKey(
            to=EnvironmetalHazardToSoilAndWater,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    vapour_emission = models.ForeignKey(
            to=VapourEmission,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
            
    @property
    def fourteen_C(self):
        value = max(extractScore(self.environmetal_hazard_to_soil_and_water_as_the_potential_to_cause.name),
                    extractScore(self.vapour_emission.name))
        return value

           
    class Meta:
        verbose_name = 'Consequence Factor Data'
        verbose_name_plural = 'Consequence Factor Data'               
    
    
    
    
    
class InspectionData(models.Model): 
    last_inspection = models.DateField(default=timezone.now)
  
    # Corrosion Rate
    minimum_thickness_measured_during_previous_inspection = models.CharField(max_length=100,
            default='5',
            verbose_name='20a: Minimum thickness measured during previous inspection')
    period_of_service_between_previous_inspection_and_this_inspection = models.CharField(max_length=100,
            default='10',
            verbose_name='20b: Period of service between previous inspection and this inspection')
    minimum_thickness_measured_during_present_inspection = models.CharField(max_length=100,
            default='5',
            verbose_name='21a: Minimum thickness measured during present inspection')
    minimum_allowable_bottom_place_thickness = models.CharField(max_length=100,
            default='4',
            verbose_name='21b: Minimum allowable bottom place thickness')
    # average_corrosion_rate_for_similar_product_tanks = models.CharField(max_length=100,
            # verbose_name='23: Average corrosion rate for similar product tanks')
    acceleration_factor_for_pitting = models.ForeignKey(
            to=AccelerationFactorForPitting,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    
    def djusted_corrosion_rate(self):
        value = None
        if self.twenty_2:
            value = (self.twenty_2 * self.acceleration_factor_for_pitting)
        else:
            value = 0.4
        return value
          
    @property
    def twenty_2(self):
        value = ((extractScore(self.minimum_thickness_measured_during_previous_inspection) - 
                  extractScore(self.minimum_thickness_measured_during_present_inspection)) / extractScore(self.period_of_service_between_previous_inspection_and_this_inspection))
        return value
            
    # Inspections
    NDT_method_used_for_thickness_measurements = models.ForeignKey(
            to=NDTMethodUsedForThicknessMeasurements,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    frequency_of_internal_inspections_performed_during_service_life = models.ForeignKey(
            to=FrequencyOfInternalInspections,
            on_delete=models.CASCADE,
            blank=True,
            null=True)
    type_of_interconnecting_bottom_plate_welds_outside_of_annular_section = models.ForeignKey(
            to=TypeOfInterconnectingBottomPlateWelds,
            on_delete=models.CASCADE,
            blank=True,
            null=True)

           
    class Meta:
        verbose_name = 'Inspection Data'
        verbose_name_plural = 'Inspection Data' 
        


class Results(models.Model): 
    # RISK ASSESSMENT
    probability_factor = models.CharField(max_length=50, default='')
    probability_rating = models.CharField(max_length=50, default='')
    economic_aspects_consequence_factor = models.CharField(max_length=50, default='')
    economic_aspects_consequence_rating = models.CharField(max_length=50, default='')
    health_and_safety_aspects_consequence_factor = models.CharField(max_length=50, default='')
    health_and_safety_aspects_consequence_rating = models.CharField(max_length=50, default='')
    environmental_aspects_consequence_factor = models.CharField(max_length=50, default='')
    environmental_aspects_consequence_rating = models.CharField(max_length=50, default='')
    overall_consequence_factor = models.CharField(max_length=50, default='')
    overall_consequence_rating = models.CharField(max_length=50, default='')
    risk_rating = models.CharField(max_length=50, default='')
    
    # REMAINING LIFE AND INSPECTION INTERVAL ASSESSMENT
    corrosion_rate = models.CharField(max_length=50, default='')
    acceleration_factor_for_pitting = models.CharField(max_length=50, default='')
    adjusted_corrosion_rate = models.CharField(max_length=50, default='')
    remaining_life = models.CharField(max_length=50, default='')
    confidence_factor = models.CharField(max_length=50, default='')
    confidence_factor_adjustement = models.CharField(max_length=50, default='')
    ajusted_confidence_factor = models.CharField(max_length=50, default='')
    interval_before_next_required_inspection = models.CharField(max_length=50, default='')
    next_inspection = models.DateField(default=timezone.now)
  
            
    class Meta:
        verbose_name = 'Results'
        verbose_name_plural = 'Results' 
        
        
        


class AllModels(models.Model):
    probability_factor_data = models.ForeignKey(
                    to=ProbabilityFactorData,
                    on_delete=models.CASCADE)
    consequence_factor_data = models.ForeignKey(
                    to=ConsequenceFactorData,
                    on_delete=models.CASCADE)
    inspection_data = models.ForeignKey(
                    to=InspectionData,
                    on_delete=models.CASCADE)
    results = models.ForeignKey(
                    to=Results,
                    on_delete=models.CASCADE)
                    
                    
                    
    
   
    
    