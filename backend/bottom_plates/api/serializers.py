from rest_framework import serializers

from bottom_plates.models import (
    ProbabilityFactorData, ConsequenceFactorData,
    InspectionData, Results 
)
from selectfields.serializers import (
    ImpressCathodicProtectionSerializer,
    SacrificialCathodicPropectionSerializer,
    BottomPlatesInternalCoatingLiningSerializer,
    BottomPlatesExternalCoatingSerializer,
    StorageConditionsSerializer,
    TypeOfBottomSerializer,
    HeatingCoilsInTankSerializer,
    ProductCorrosivitySerializer,
    FoundationTypeSerializer,
    HeightOfFoundationSerializer,
    EffectivenessOfDrainageSerializer,
    TimeToRepairSerializer,
    CostOfRepairSerializer,
    ProbableMagnitudeOfProductLossSerializer,
    LikelihoodOfInjuryToPersonnelSerializer,
    ProductFlammabilityAsPerMCSPSerializer,
    ProductToxicitySerializer,
    LocationOfTankFarmSerializer,
    EnvironmetalHazardToSoilAndWaterSerializer,
    VapourEmissionSerializer,
    AccelerationFactorForPittingSerializer,
    NDTMethodUsedForThicknessMeasurementsSerializer,
    FrequencyOfInternalInspectionsSerializer,
    TypeOfInterconnectingBottomPlateWeldsSerializer,
)



class ProbabilityFactorDataSerializer(serializers.ModelSerializer):
    impresses_cathodic_protect = ImpressCathodicProtectionSerializer()
    sacrificial_cathodic_propect = SacrificialCathodicPropectionSerializer()
    bottom_plates_internal_coating_or_linin = BottomPlatesInternalCoatingLiningSerializer()
    bottom_plates_external_coatin = BottomPlatesExternalCoatingSerializer()
    storage_condition = StorageConditionsSerializer()
    types_of_bottom = TypeOfBottomSerializer()
    heating_coils_in_tanks = HeatingCoilsInTankSerializer()
    products_corrosivity = ProductCorrosivitySerializer()
    foundation_types = FoundationTypeSerializer()
    heights_of_foundation = HeightOfFoundationSerializer()
    effectiveness_of_drainages = EffectivenessOfDrainageSerializer()
    
    class Meta:
        model = ProbabilityFactorData
        fields = ['id', 'impresses_cathodic_protect',
                  'sacrificial_cathodic_propect',
                  'bottom_plates_internal_coating_or_linin',
                  'bottom_plates_external_coatin',
                  'storage_condition', 'types_of_bottom',
                  'heating_coils_in_tanks', 'products_corrosivity',
                  'foundation_types', 'heights_of_foundation',
                  'effectiveness_of_drainages']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['score_five'] = instance.five_score
        return data
        
        

class ConsequenceFactorDataSerializer(serializers.ModelSerializer):
    time_to_repair = TimeToRepairSerializer()
    cost_of_repair = CostOfRepairSerializer()
    probable_magnitude_of_product_loss = ProbableMagnitudeOfProductLossSerializer()
    likelihood_of_injury_to_personnel = LikelihoodOfInjuryToPersonnelSerializer()
    product_flammability_as_per_MCSP = ProductFlammabilityAsPerMCSPSerializer()
    product_toxicity = ProductToxicitySerializer()
    location_of_tank_farm = LocationOfTankFarmSerializer()
    environmetal_hazard_to_soil_and_water_as_the_potential_to_cause = EnvironmetalHazardToSoilAndWaterSerializer()
    vapour_emission = VapourEmissionSerializer()
    
    class Meta:
        model = ConsequenceFactorData
        fields = ['id', 'time_to_repair', 
                  'cost_of_repair', 
                  'probable_magnitude_of_product_loss',
                  'likelihood_of_injury_to_personnel',
                  'product_flammability_as_per_MCSP',
                  'product_toxicity', 'location_of_tank_farm',
                  'environmetal_hazard_to_soil_and_water_as_the_potential_to_cause',
                  'vapour_emission']
        # depth = 1
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ten_D_score'] = instance.ten_D_score
        data['twelve_E_score'] = instance.twelve_E
        data['fourteen_C_score'] = instance.fourteen_C
        return data
        
      
      
class InspectionDataSerializer(serializers.ModelSerializer):
    last_inspection = serializers.DateField()
    minimum_thickness_measured_during_previous_inspection = serializers.CharField(max_length=100)
    period_of_service_between_previous_inspection_and_this_inspection = serializers.CharField(max_length=100)
    minimum_thickness_measured_during_present_inspection = serializers.CharField(max_length=100)
    minimum_allowable_bottom_place_thickness = serializers.CharField(max_length=100)
    acceleration_factor_for_pitting = AccelerationFactorForPittingSerializer()
    NDT_method_used_for_thickness_measurements = NDTMethodUsedForThicknessMeasurementsSerializer()
    frequency_of_internal_inspections_performed_during_service_life = FrequencyOfInternalInspectionsSerializer()
    type_of_interconnecting_bottom_plate_welds_outside_of_annular_section = TypeOfInterconnectingBottomPlateWeldsSerializer()
    
    class Meta:
        model = InspectionData
        fields = '__all__'
        depth = 1
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['twenty_2_score'] = instance.twenty_2
        return data
        
        
        
        
class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'