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
    class Meta:
        model = ConsequenceFactorData
        fields = '__all__'
        depth = 1
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ten_D_score'] = instance.ten_D_score
        data['twelve_E_score'] = instance.twelve_E
        data['fourteen_C_score'] = instance.fourteen_C
        return data
        
      
      
class InspectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionData
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['twenty_2_score'] = instance.twenty_2
        return data