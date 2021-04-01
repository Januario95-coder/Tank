from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import (
    ProbabilityFactorData,
    ConsequenceFactorData,
)
from .serializers import (
    ProbabilityFactorDataSerializer,
    ConsequenceFactorDataSerializer,
)



class ProbabilityFactorDataView(generics.ListAPIView):
    serializer_class = ProbabilityFactorDataSerializer
    queryset = ProbabilityFactorData.objects.all()
    
    
class ConsequenceFactorDataView(generics.ListAPIView):
    serializer_class = ConsequenceFactorDataSerializer
    queryset = ConsequenceFactorData.objects.all()