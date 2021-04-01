from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from .models import Project
from .serializers import (
    ProjectSerializer,
    UserSerializer,
)

from bottom_plates.models import (
    ProbabilityFactorData,
    ConsequenceFactorData,
    InspectionData
)

from selectfields.models import (
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
    NDTMethodUsedForThicknessMeasurements,
    FrequencyOfInternalInspections,
    TypeOfInterconnectingBottomPlateWelds,
)

import json
from datetime import datetime


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
    

@require_POST
@csrf_exempt
def create_project(request):
    data = json.loads(request.body)
    print(data)
    start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
    project = Project.objects.create(
        name=data['name'], 
        description=data['description'], 
        start_date=start_date,
        end_date=end_date,
    )
    return JsonResponse({
        'message': 'Project created successfully'
    })



def filtering_function(data, name):
    try:
        filtering = data[name]['name']
    except (TypeError, IndexError):
        filtering = data[name]
    return filtering
    

@require_POST
@csrf_exempt
def update_project_details(request):
    data = json.loads(request.body)
    project = Project.objects.filter(id=data['id'])
    proj = None
    message = None
    print(data)

    if project.exists():
        proj = project.first()
        message = "Project exists."
        probability_factor_data = ProbabilityFactorData.objects.get(id=proj.default_values.probability_factor_data.id)

        filtering = filtering_function(data, 'impressCathodProtectionValue')
        impresses_cathodic_protect = ImpressCathodicProtection.objects.filter(name__icontains=filtering)
        if impresses_cathodic_protect.exists():
            first = impresses_cathodic_protect.first()
            probability_factor_data.impresses_cathodic_protect = first
        
        filtering = filtering_function(data, 'sacriCathProteValue')
        sacrificial_cathodic_propect = SacrificialCathodicPropection.objects.filter(name__icontains=filtering)
        if sacrificial_cathodic_propect.exists():
            first = sacrificial_cathodic_propect.first()
            probability_factor_data.sacrificial_cathodic_propect = first
        
        filtering = filtering_function(data, 'bottomPlatesInternalCoatingValue')
        bottom_plates_internal_coating = BottomPlatesInternalCoatingLining.objects.filter(name__icontains=filtering)
        if bottom_plates_internal_coating.exists():
            first = bottom_plates_internal_coating.first()
            probability_factor_data.bottom_plates_internal_coating_or_linin = first
        
        filtering = filtering_function(data, 'bottomPlatesExternalCoatingValue')
        bottom_plates_external_coating = BottomPlatesExternalCoating.objects.filter(name__icontains=filtering)
        if bottom_plates_external_coating.exists():
            first = bottom_plates_external_coating.first()
            probability_factor_data.bottom_plates_external_coatin = first
          
        filtering = filtering_function(data, 'storageConditionValue')
        storage_condition = StorageConditions.objects.filter(name__icontains=filtering)
        if storage_condition.exists():
            first = storage_condition.first()
            probability_factor_data.storage_condition = first

        filtering = filtering_function(data, 'typeOfBottonValue')
        types_of_bottom = TypeOfBottom.objects.filter(name__icontains=filtering)
        if types_of_bottom.exists():
            first = types_of_bottom.first()
            probability_factor_data.types_of_bottom = first
        
        filtering = filtering_function(data, 'heatingCoilsInTankValue')
        heating_coils_in_tanks = HeatingCoilsInTank.objects.filter(name__icontains=filtering)
        if heating_coils_in_tanks.exists():
            first = heating_coils_in_tanks.first()
            probability_factor_data.heating_coils_in_tanks = first
            
        filtering = filtering_function(data, 'productCorrosivityValue')
        products_corrosivity = ProductCorrosivity.objects.filter(name__icontains=filtering)
        if products_corrosivity.exists():
            first = products_corrosivity.first()
            probability_factor_data.products_corrosivity = first
            
        filtering = filtering_function(data, 'foundationTypeValue')
        foundation_types = FoundationType.objects.filter(name__icontains=filtering)
        if foundation_types.exists():
            first = foundation_types.first()
            probability_factor_data.foundation_types = first
            
        filtering = filtering_function(data, 'heightOfFoundationValue')
        heights_of_foundation = HeightOfFoundation.objects.filter(name__icontains=filtering)
        if heights_of_foundation.exists():
            first = heights_of_foundation.first()
            probability_factor_data.heights_of_foundation = first
            
        filtering = filtering_function(data, 'effectiveDrainageValue')
        effectiveness_of_drainages = EffectivenessOfDrainage.objects.filter(name__icontains=filtering)
        if effectiveness_of_drainages.exists():
            first = effectiveness_of_drainages.first()
            probability_factor_data.effectiveness_of_drainages = first
            
        probability_factor_data.save()
        
            
        consequence_factor_data = ConsequenceFactorData.objects.get(id=proj.default_values.consequence_factor_data.id)
        filtering = filtering_function(data, 'timeToRepairValue')
        time_to_repair = TimeToRepair.objects.filter(name__icontains=filtering)
        if time_to_repair.exists():
            first = time_to_repair.first()
            consequence_factor_data.time_to_repair = first
        
        filtering = filtering_function(data, 'costOfRepairValue')
        cost_of_repair = CostOfRepair.objects.filter(name__icontains=filtering)
        if cost_of_repair.exists():
            first = cost_of_repair.first()
            consequence_factor_data.cost_of_repair = first
        
        consequence_factor_data.save()
        
    else:
        message = f"Project with id = {data['id']} does not exis"
        
    # print(message)
    
    return JsonResponse({
        'message': 'Data Received'
    })
    
    
@require_POST
@csrf_exempt
def update_project(request):
    data = json.loads(request.body)
    project = Project.objects.filter(id=data['id'])
    if project.exists():
        obj = project.first()
        obj.name = data['name']
        obj.description = data['description']
        obj.start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
        obj.end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
        obj.save()
    return JsonResponse({
        'message': 'Project was updated successfully'
    })
    
    
def get_user(request):
    user = None
    # if request.user.is_authenticated:
        # user = request.user.username
    # else:
        # user = 'Anonymous'
    user = User.objects.filter(is_superuser=True)
    user = user.first().username
    return JsonResponse({
        'user': user
    })


@require_POST
@csrf_exempt
def delete_project(request):
    data = json.loads(request.body)
    project = Project.objects.filter(pk=data['id'])
    message = None
    if project.exists():
        obj = project.first()
        obj.delete()
        message = "Project was deleted successfully"
    else:
        message = "Project was not delete"
    return JsonResponse({
        'message': message
    })
    