from rest_framework.viewsets import ModelViewSet

from .serializers import (
    impressedCoatingAppliedToSheelPlatesSerializer,
    ExternalCoatingAppliedToShellPlatesSerializer,
    StorageConditionsSerializer,
    HeatedCoilsInTankSerializer,
    ProductCorrosivitySerializer,
    VaporCorrosivitySerializer,
    TankShellHasBeenInsulatedSerializer,
)


from .models import (
    impressedCoatingAppliedToSheelPlates,
    ExternalCoatingAppliedToShellPlates,
    StorageConditions,
    HeatedCoilsInTank,
    ProductCorrosivity,
    VaporCorrosivity,
    TankShellHasBeenInsulated,
)



class impressedCoatingAppliedToSheelPlatesView(ModelViewSet):  
    serializer_class = impressedCoatingAppliedToSheelPlatesSerializer
    queryset = impressedCoatingAppliedToSheelPlates.objects.all()
    


class ExternalCoatingAppliedToShellPlatesView(ModelViewSet):  
    serializer_class = ExternalCoatingAppliedToShellPlatesSerializer
    queryset = ExternalCoatingAppliedToShellPlates.objects.all()
    
    
class StorageConditionsView(ModelViewSet):  
    serializer_class = StorageConditionsSerializer
    queryset = StorageConditions.objects.all()
    
    
class HeatedCoilsInTankView(ModelViewSet):  
    serializer_class = HeatedCoilsInTankSerializer
    queryset = HeatedCoilsInTank.objects.all()
    
    
class ProductCorrosivityView(ModelViewSet):  
    serializer_class = ProductCorrosivitySerializer
    queryset = ProductCorrosivity.objects.all()
      

class VaporCorrosivityView(ModelViewSet):  
    serializer_class = VaporCorrosivitySerializer
    queryset = VaporCorrosivity.objects.all()
    

class TankShellHasBeenInsulatedView(ModelViewSet):  
    serializer_class = TankShellHasBeenInsulatedSerializer
    queryset = TankShellHasBeenInsulated.objects.all()
    
    
    
    
    
    
    
    
    
    
    
    
    
# class HeightOfFoundationView(ModelViewSet):  
    # serializer_class = HeightOfFoundationSerializer
    # queryset = HeightOfFoundation.objects.all()
    
    
# class EffectivenessOfDrainageView(ModelViewSet):  
    # serializer_class = EffectivenessOfDrainageSerializer
    # queryset = EffectivenessOfDrainage.objects.all()
    

# class TimeToRepairView(ModelViewSet):  
    # serializer_class = TimeToRepairSerializer
    # queryset = TimeToRepair.objects.all()
    
    
# class CostOfRepairView(ModelViewSet):  
    # serializer_class = CostOfRepairSerializer
    # queryset = CostOfRepair.objects.all()
    
    
# class ProbableMagnitudeOfProductLossView(ModelViewSet):  
    # serializer_class = ProbableMagnitudeOfProductLossSerializer
    # queryset = ProbableMagnitudeOfProductLoss.objects.all()
    
    
# class LikelihoodOfInjuryToPersonnelView(ModelViewSet):  
    # serializer_class = LikelihoodOfInjuryToPersonnelSerializer
    # queryset = LikelihoodOfInjuryToPersonnel.objects.all()
    


# class ProductFlammabilityAsPerMCSPView(ModelViewSet):  
    # serializer_class = ProductFlammabilityAsPerMCSPSerializer
    # queryset = ProductFlammabilityAsPerMCSP.objects.all()
    

# class ProductToxicityView(ModelViewSet):  
    # serializer_class = ProductToxicitySerializer
    # queryset = ProductToxicity.objects.all()

    
# class LocationOfTankFarmView(ModelViewSet):  
    # serializer_class = LocationOfTankFarmSerializer
    # queryset = LocationOfTankFarm.objects.all()
    
    
# class EnvironmetalHazardToSoilAndWaterView(ModelViewSet):  
    # serializer_class = EnvironmetalHazardToSoilAndWaterSerializer
    # queryset = EnvironmetalHazardToSoilAndWater.objects.all()


# class VapourEmissionView(ModelViewSet):  
    # serializer_class = VapourEmissionSerializer
    # queryset = VapourEmission.objects.all()
    
    
# class AccelerationFactorForPittingView(ModelViewSet):  
    # serializer_class = AccelerationFactorForPittingSerializer
    # queryset = AccelerationFactorForPitting.objects.all()
    
    
# class NDTMethodUsedForThicknessMeasurementsView(ModelViewSet):  
    # serializer_class = NDTMethodUsedForThicknessMeasurementsSerializer
    # queryset = NDTMethodUsedForThicknessMeasurements.objects.all()
    
    
# class FrequencyOfInternalInspectionsView(ModelViewSet):  
    # serializer_class = FrequencyOfInternalInspectionsSerializer
    # queryset = FrequencyOfInternalInspections.objects.all()
    
    
# class TypeOfInterconnectingBottomPlateWeldsView(ModelViewSet):  
    # serializer_class = TypeOfInterconnectingBottomPlateWeldsSerializer
    # queryset = TypeOfInterconnectingBottomPlateWelds.objects.all()
    
    
    