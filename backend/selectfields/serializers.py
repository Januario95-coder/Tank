from rest_framework import serializers

from .models import (
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



def formatName(name):
    return name.split('-')[0].strip()
    # name = name.split('-') 
    # if len(name) > 2:
        # return '-'.join(name[:2])
    # return name[0].strip()

    

class NameFormatting:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = formatName(instance.name)
        return data


class ImpressCathodicProtectionSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    
    class Meta:
        model = ImpressCathodicProtection
        fields = ['id', 'name']
        
        
class SacrificialCathodicPropectionSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = SacrificialCathodicPropection
        fields = ['id', 'name']

        
        
class BottomPlatesInternalCoatingLiningSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = BottomPlatesInternalCoatingLining
        fields = ['id', 'name']

        
        
        
class BottomPlatesExternalCoatingSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = BottomPlatesExternalCoating
        fields = ['id', 'name']   
        
        
class StorageConditionsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = StorageConditions
        fields = ['id', 'name']

        
        
class TypeOfBottomSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = TypeOfBottom
        fields = ['id', 'name']

        
class HeatingCoilsInTankSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = HeatingCoilsInTank
        fields = ['id', 'name']

        

class ProductCorrosivitySerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProductCorrosivity
        fields = ['id', 'name']

        
class FoundationTypeSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = FoundationType
        fields = ['id', 'name']
        
        
        
class HeightOfFoundationSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = HeightOfFoundation
        fields = ['id', 'name']

        
        
class EffectivenessOfDrainageSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = EffectivenessOfDrainage
        fields = ['id', 'name']
        
        
class TimeToRepairSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = TimeToRepair
        fields = ['id', 'name']
        
        
        
class CostOfRepairSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = CostOfRepair
        fields = ['id', 'name']

        
        
class ProbableMagnitudeOfProductLossSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProbableMagnitudeOfProductLoss
        fields = ['id', 'name']

        
class LikelihoodOfInjuryToPersonnelSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = LikelihoodOfInjuryToPersonnel
        fields = ['id', 'name']

        
        
class ProductFlammabilityAsPerMCSPSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProductFlammabilityAsPerMCSP
        fields = ['id', 'name']
        
        
class ProductToxicitySerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = ProductToxicity
        fields = ['id', 'name']
        
        
        
class LocationOfTankFarmSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = LocationOfTankFarm
        fields = ['id', 'name']

        
        
class EnvironmetalHazardToSoilAndWaterSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = EnvironmetalHazardToSoilAndWater
        fields = ['id', 'name']

        
        
class VapourEmissionSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = VapourEmission
        fields = ['id', 'name']
        
        
class AccelerationFactorForPittingSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = AccelerationFactorForPitting
        fields = ['id', 'name']
        
        

class NDTMethodUsedForThicknessMeasurementsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = NDTMethodUsedForThicknessMeasurements
        fields = ['id', 'name']

        
        
class FrequencyOfInternalInspectionsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = FrequencyOfInternalInspections
        fields = ['id', 'name']

        
        
class TypeOfInterconnectingBottomPlateWeldsSerializer(
    NameFormatting,
    serializers.ModelSerializer):
    class Meta:
        model = TypeOfInterconnectingBottomPlateWelds
        fields = ['id', 'name']
