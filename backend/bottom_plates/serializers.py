from rest_framework import serializers

from .models import (
    ProbabilityFactorData,
    ConsequenceFactorData
)



class ProbabilityFactorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProbabilityFactorData
        fields = '__all__'
        
        
        
class ConsequenceFactorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsequenceFactorData
        fields = ['id', 'time_to_repair', 'cost_of_repair', 
                  'probable_magnitude_of_product_loss',
                   
                  'likelihood_of_injury_to_personnel',
                  'product_flammability_as_per_MCSP',
                  'product_toxicity',
                  'location_of_tank_farm',
                  'continued_location_of_tank_farm',
                   
                  'environmetal_hazard_to_soil_and_water_as_the_potential_to_cause',
                  'vapour_emission']
                  
        
        

