from django.db import models

from bottom_plates.INPUT_FIELDS_SELECTION import *
from shell_plates.INPUT_FIELDS_SELECTION import *



class impressedCoatingAppliedToSheelPlates(models.Model):
    name = models.CharField(max_length=100,
            choices=IMPRESSED_COATING_APPLIED_TO_SHEEL_PLATES,
            default='Internal coating applied and quality is sound - score=0',
            verbose_name='1: impressed Coating Applied To Sheel Plates'
    )
    
    def __str__(self):
        return self.name
        
        

class ExternalCoatingAppliedToShellPlates(models.Model):
    name = models.CharField(max_length=100,
            choices=EXTERNAL_COATING_APPLIED_TO_SHELL_PLATES,
            default='External coating applied and quality is sound - score=0',
            verbose_name='External Coating Applied To Shell Plates'
    )
    
    def __str__(self):
        return self.name
        
      
DEGREE_SIGN = u'\N{DEGREE SIGN}'
        
class StorageConditions(models.Model):
    name = models.CharField(max_length=100,
            choices=STORAGE_CONDITIONS,
            default=f'Temperature of product < 40{DEGREE_SIGN}C - score=0',
            verbose_name='Storage conditions'
    )
    
    def __str__(self):
        return self.name



class HeatedCoilsInTank(models.Model):
    name = models.CharField(max_length=100,
            choices=HEATING_COILS_IN_TANK,
            default='No heating coil or no contact between heating coil and shell plates - score=0',
            verbose_name='Heated coils in tank'
    )
    
    def __str__(self):
        return self.name
        
        
        
class ProductCorrosivity(models.Model):
    name = models.CharField(max_length=100,
            choices=PRODUCT_CORROSIVITY,
            default='Product group 4 - score=2',
            verbose_name='Product corrosivity'
    )
    
    def __str__(self):
        return self.name
        


class VaporCorrosivity(models.Model):
    name = models.CharField(max_length=100,
            choices=VAPOUR_CORROSIVITY,
            default='Vapour group 4 - score=2',
            verbose_name='Vapor corrosivity'
    )
    
    def __str__(self):
        return self.name
     
        
class TankShellHasBeenInsulated(models.Model):
    name = models.CharField(max_length=100,
            choices=TANK_SHELL_HAS_BEEN_INSULATED,
            default='CUI is likely to occur - score=2',
            verbose_name='Tank shell has been insulated, and rain water may cause corrosion under insulation (CUI')
    
    def __str__(self):
        return self.name
    
    
        
        
        
        

# class FoundationType(models.Model):
    # name = models.CharField(max_length=100,
            # choices=FOUNDATION_TYPE,
            # default='Piled concrete raft - Score=0',
            # verbose_name='7: Foundation type'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Foundation Type'
        # verbose_name_plural = 'Foundation Type'
            
            

# class HeightOfFoundation(models.Model):
    # name = models.CharField(max_length=100,
            # choices=HEIGHT_OF_FOUNDATION,
            # default='Tank bottom free from contact with water - Score=0',
            # verbose_name='8: Height of foundation')
            
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Height Of Foundation'
        # verbose_name_plural = 'Height Of Foundation'
            
            
# class EffectivenessOfDrainage(models.Model):
    # name = models.CharField(max_length=150,
            # choices=EFFECTIVENESS_OF_DRAINAGE,
            # default='Slope of tank pad shoulder allows for adequate drainage away from tank bottom - Score=0',
            # verbose_name='9: Effectiveness of drainage')
           
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Effectiveness Of Drainage'
        # verbose_name_plural = 'Effectiveness Of Drainage'
        
        

# class TimeToRepair(models.Model):
    # name = models.CharField(max_length=100,
            # choices=TIME_TO_REPAIR,
            # default='No internal entry required limited repair, no limitation on repair time - Score=1',
            # verbose_name='10a: Time to repair'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Time To Repair'
        # verbose_name_plural = 'Time To Repair'
    
    
    
# class CostOfRepair(models.Model):
    # name = models.CharField(max_length=100,
            # choices=COST_OF_REPAIR,
            # default='Negligible or less than 5% of capital cost - Score=1',
            # verbose_name='10b: Cost of repair'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Cost Of Repair'
        # verbose_name_plural = 'Cost Of Repair'
    
    
    
# class ProbableMagnitudeOfProductLoss(models.Model):
    # name = models.CharField(max_length=100,
            # choices=PROBABLE_MAGNITUDE_OF_PRODUCT_LOSS,
            # default='No release of product - Score=1',
            # verbose_name='10c: Probable magnitude of product loss'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Probable Magnitude Of ProductLoss'
        # verbose_name_plural = 'Probable Magnitude Of Product Loss'
        
        

# class LikelihoodOfInjuryToPersonnel(models.Model):
    # name = models.CharField(max_length=100,
            # choices=LIKELIHOOD_OF_INJURY_TO_PERSONNEL,
            # default='No injury or near miss - Score=1',
            # verbose_name='12a: Likelihood of injury to personnel'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Likelihood Of Injury To Personnel'
        # verbose_name_plural = 'Likelihood Of Injury To Personnel'
    
    

# class ProductFlammabilityAsPerMCSP(models.Model):
    # name = models.CharField(max_length=100,
            # choices=PRODUCT_FLAMMABILITY_AS_PER_MCSP,
            # default='Class III(1) and unclassified product - Score=1',
            # verbose_name='12b: Product flammability as per MCSP'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Product Flammability As Per MCSP'
        # verbose_name_plural = 'Product Flammability As Per MCSP'
    
    
    

# class ProductToxicity(models.Model):
    # name = models.CharField(max_length=100,
            # choices=PRODUCT_TOXICITY,
            # default='Non-toxic substances- Score=1',
            # verbose_name='12c: Product toxicity'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Product Toxicity'
        # verbose_name_plural = 'Product Toxicity'
    
    
    
# class LocationOfTankFarm(models.Model):
    # name = models.CharField(max_length=100,
            # choices=LOCATION_OF_TANK_FARM,
            # default='Tank farm within an abandonned area - Score=1',
            # verbose_name='12d: Location of tank farm')
            
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Location Of Tank Farm'
        # verbose_name_plural = 'Location Of Tank Farm'
        
        

# class EnvironmetalHazardToSoilAndWater(models.Model):
    # name = models.CharField(max_length=100,
            # choices=ENVIRONMETAL_HAZARD_TO_SOIL_AND_WATER_AS_THE_POTENTIAL_TO_CAUSE,
            # default='Nor or negligle environment effect - Score=1',
            # verbose_name='14a: Environmetal hazard to soil and water as the potential to cause'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Environmetal Hazard To Soil And Water'
        # verbose_name_plural = 'Environmetal Hazard To Soil And Water'
    
    
    
# class VapourEmission(models.Model):
    # name = models.CharField(max_length=100,
            # choices=VAPOUR_EMISSION,
            # default='No or negligle harmful (toxic) release - Score=1',
            # verbose_name='14b: Vapour emission')
            
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Vapour Emission'
        # verbose_name_plural = 'Vapour Emission'
        
        
        
# class AccelerationFactorForPitting(models.Model):
    # name = models.CharField(max_length=100,
            # choices=ACCELERATION_FACTOR_FOR_PITTING,
            # verbose_name='24. Acceleration factor for pitting',
            # default='1.15'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Acceleration Factor For Pitting'
        # verbose_name_plural = 'Acceleration Factor For Pitting'
        
        
    
# class NDTMethodUsedForThicknessMeasurements(models.Model):
    # name = models.CharField(max_length=100,
            # choices=NDT_METHOD_USED_FOR_THICKNESS_MEASUREMENTS,
            # default='Floor scan + US - Score=-0.1',
            # verbose_name='28: NDT method used for thickness measurements'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'NDT Method Used For Thickness Measurements'
        # verbose_name_plural = 'NDT Method Used For Thickness Measurements'
    
    
    
# class FrequencyOfInternalInspections(models.Model):
    # name = models.CharField(max_length=100,
            # choices=FREQUENCY_OF_INTERNAL_INSPECTIONS_PERFORMED_DURING_SERVICE_LIFE,
            # default='Multiple inspections carried out - Score=0.1',
            # verbose_name='29: Frequency of internal inspections performed during service life'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Frequency Of Internal Inspections'
        # verbose_name_plural = 'Frequency Of Internal Inspections'
    
    
    
# class TypeOfInterconnectingBottomPlateWelds(models.Model):
    # name = models.CharField(max_length=100,
            # choices=TYPE_OF_INTERCONNECTING_BOTTOM_PLATE_WELDS_OUTSIDE_OF_ANNULAR_SECTION,
            # default='Butt welds - Score=0.1',
            # verbose_name='30: Type of interconnecting bottom plate welds outside of annular section'
    # )
    
    # def __str__(self):
        # return self.name
    
    # class Meta:
        # verbose_name = 'Type Of Interconnecting Bottom Plate Welds'
        # verbose_name_plural = 'Type Of Interconnecting Bottom Plate Welds'
    
    