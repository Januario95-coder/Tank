from rest_framework.viewsets import ModelViewSet

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



class ImpressCathodicProtectionView(ModelViewSet):  
    serializer_class = ImpressCathodicProtectionSerializer
    queryset = ImpressCathodicProtection.objects.all()
    


class SacrificialCathodicPropectionView(ModelViewSet):  
    serializer_class = SacrificialCathodicPropectionSerializer
    queryset = SacrificialCathodicPropection.objects.all()
    
    
class BottomPlatesInternalCoatingLiningView(ModelViewSet):  
    serializer_class = BottomPlatesInternalCoatingLiningSerializer
    queryset = BottomPlatesInternalCoatingLining.objects.all()
    
    
class BottomPlatesExternalCoatingView(ModelViewSet):  
    serializer_class = BottomPlatesExternalCoatingSerializer
    queryset = BottomPlatesExternalCoating.objects.all()
    
    
class StorageConditionsView(ModelViewSet):  
    serializer_class = StorageConditionsSerializer
    queryset = StorageConditions.objects.all()
    

class TypeOfBottomView(ModelViewSet):  
    serializer_class = TypeOfBottomSerializer
    queryset = TypeOfBottom.objects.all()
    
    
class HeatingCoilsInTankView(ModelViewSet):  
    serializer_class = HeatingCoilsInTankSerializer
    queryset = HeatingCoilsInTank.objects.all()
    
    
class ProductCorrosivityView(ModelViewSet):  
    serializer_class = ProductCorrosivitySerializer
    queryset = ProductCorrosivity.objects.all()
    
    
class FoundationTypeView(ModelViewSet):  
    serializer_class = FoundationTypeSerializer
    queryset = FoundationType.objects.all()
    
    
class HeightOfFoundationView(ModelViewSet):  
    serializer_class = HeightOfFoundationSerializer
    queryset = HeightOfFoundation.objects.all()
    
    
class EffectivenessOfDrainageView(ModelViewSet):  
    serializer_class = EffectivenessOfDrainageSerializer
    queryset = EffectivenessOfDrainage.objects.all()
    

class TimeToRepairView(ModelViewSet):  
    serializer_class = TimeToRepairSerializer
    queryset = TimeToRepair.objects.all()
    
    
class CostOfRepairView(ModelViewSet):  
    serializer_class = CostOfRepairSerializer
    queryset = CostOfRepair.objects.all()
    
    
class ProbableMagnitudeOfProductLossView(ModelViewSet):  
    serializer_class = ProbableMagnitudeOfProductLossSerializer
    queryset = ProbableMagnitudeOfProductLoss.objects.all()
    
    
class LikelihoodOfInjuryToPersonnelView(ModelViewSet):  
    serializer_class = LikelihoodOfInjuryToPersonnelSerializer
    queryset = LikelihoodOfInjuryToPersonnel.objects.all()
    


class ProductFlammabilityAsPerMCSPView(ModelViewSet):  
    serializer_class = ProductFlammabilityAsPerMCSPSerializer
    queryset = ProductFlammabilityAsPerMCSP.objects.all()
    

class ProductToxicityView(ModelViewSet):  
    serializer_class = ProductToxicitySerializer
    queryset = ProductToxicity.objects.all()

    
class LocationOfTankFarmView(ModelViewSet):  
    serializer_class = LocationOfTankFarmSerializer
    queryset = LocationOfTankFarm.objects.all()
    
    
class EnvironmetalHazardToSoilAndWaterView(ModelViewSet):  
    serializer_class = EnvironmetalHazardToSoilAndWaterSerializer
    queryset = EnvironmetalHazardToSoilAndWater.objects.all()


class VapourEmissionView(ModelViewSet):  
    serializer_class = VapourEmissionSerializer
    queryset = VapourEmission.objects.all()
    
    
class AccelerationFactorForPittingView(ModelViewSet):  
    serializer_class = AccelerationFactorForPittingSerializer
    queryset = AccelerationFactorForPitting.objects.all()
    
    
class NDTMethodUsedForThicknessMeasurementsView(ModelViewSet):  
    serializer_class = NDTMethodUsedForThicknessMeasurementsSerializer
    queryset = NDTMethodUsedForThicknessMeasurements.objects.all()
    
    
class FrequencyOfInternalInspectionsView(ModelViewSet):  
    serializer_class = FrequencyOfInternalInspectionsSerializer
    queryset = FrequencyOfInternalInspections.objects.all()
    
    
class TypeOfInterconnectingBottomPlateWeldsView(ModelViewSet):  
    serializer_class = TypeOfInterconnectingBottomPlateWeldsSerializer
    queryset = TypeOfInterconnectingBottomPlateWelds.objects.all()
    
    
    