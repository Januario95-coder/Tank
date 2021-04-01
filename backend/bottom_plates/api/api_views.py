from rest_framework.viewsets import ModelViewSet

from .serializers import (
    ProbabilityFactorDataSerializer,
    ConsequenceFactorDataSerializer,
    InspectionDataSerializer
)
from bottom_plates.models import (
    ProbabilityFactorData, ConsequenceFactorData,
    ConsequenceFactorData,
    InspectionData, Results
)



class ProbabilityFactorDataView(ModelViewSet):
    serializer_class = ProbabilityFactorDataSerializer
    queryset = ProbabilityFactorData.objects.all()
    


class ConsequenceFactorView(ModelViewSet):
    serializer_class = ConsequenceFactorDataSerializer
    queryset = ConsequenceFactorData.objects.all()


class InspectionDataView(ModelViewSet):
    serializer_class = InspectionDataSerializer
    queryset = InspectionData.objects.all()