from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Project
from bottom_plates.models import AllModels

from bottom_plates.api.serializers import (
    ProbabilityFactorDataSerializer,
    ConsequenceFactorDataSerializer,
    InspectionDataSerializer
)


class AllModelsSerializer(serializers.ModelSerializer):
    probability_factor_data = ProbabilityFactorDataSerializer()
    consequence_factor_data = ConsequenceFactorDataSerializer()
    inspection_data = InspectionDataSerializer()
    
    class Meta:
        model = AllModels
        fields = ['id', 'probability_factor_data',
                  'consequence_factor_data',
                  'inspection_data']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username']
        

class ProjectSerializer(serializers.ModelSerializer):
    default_values = AllModelsSerializer()
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description',
                  'start_date', 'end_date',
                  'default_values']
        # depth = 3
                  
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
        
        