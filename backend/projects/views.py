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
    InspectionData,
    Results
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
    AccelerationFactorForPitting,
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
    
    
def update_field(func, data, keyValue, model):
    filtering = func(data, keyValue)
    sacrificial_cathodic_propect = model.objects.filter(name__icontains=filtering)
    if sacrificial_cathodic_propect.exists():
        first = sacrificial_cathodic_propect.first()
        return first
    return ''
    

@require_POST
@csrf_exempt
def update_project_details(request):
    data = json.loads(request.body)
    project = Project.objects.filter(id=data['id'])
    proj = None
    message = None
    print('\n', data, '\n')

    if project.exists():
        proj = project.first()
        message = "Project exists."
        probability_factor_data = ProbabilityFactorData.objects.get(id=proj.default_values.probability_factor_data.id)
        
        impresses_cathodic_protect = update_field(filtering_function, data, 'impressCathodProtectionValue', ImpressCathodicProtection)
        probability_factor_data.impresses_cathodic_protect = impresses_cathodic_protect
        
        sacrificial_cathodic_propect = update_field(filtering_function, data, 'sacriCathProteValue', SacrificialCathodicPropection)
        probability_factor_data.sacrificial_cathodic_propect = sacrificial_cathodic_propect
        
        bottom_plates_internal_coating_or_linin = update_field(filtering_function, data, 'bottomPlatesInternalCoatingValue', BottomPlatesInternalCoatingLining)
        probability_factor_data.bottom_plates_internal_coating_or_linin = bottom_plates_internal_coating_or_linin
            
        bottom_plates_external_coatin = update_field(filtering_function, data, 'bottomPlatesExternalCoatingValue', BottomPlatesExternalCoating)
        probability_factor_data.bottom_plates_external_coatin = bottom_plates_external_coatin
            
        storage_condition = update_field(filtering_function, data, 'storageConditionValue', StorageConditions)
        probability_factor_data.storage_condition = storage_condition
            
        types_of_bottom = update_field(filtering_function, data, 'typeOfBottonValue', TypeOfBottom)
        probability_factor_data.types_of_bottom = types_of_bottom
            
        heating_coils_in_tanks = update_field(filtering_function, data, 'heatingCoilsInTankValue', HeatingCoilsInTank)
        probability_factor_data.heating_coils_in_tanks = heating_coils_in_tanks
            
        products_corrosivity = update_field(filtering_function, data, 'productCorrosivityValue', ProductCorrosivity)
        probability_factor_data.products_corrosivity = products_corrosivity
            
        foundation_types = update_field(filtering_function, data, 'foundationTypeValue', FoundationType)
        probability_factor_data.foundation_types = foundation_types
            
        heights_of_foundation = update_field(filtering_function, data, 'heightOfFoundationValue', HeightOfFoundation)
        probability_factor_data.heights_of_foundation = heights_of_foundation
            
        effectiveness_of_drainages = update_field(filtering_function, data, 'effectiveDrainageValue', EffectivenessOfDrainage)
        probability_factor_data.effectiveness_of_drainages = effectiveness_of_drainages
            
        probability_factor_data.save()
        
        
        
            
        consequence_factor_data = ConsequenceFactorData.objects.get(id=proj.default_values.consequence_factor_data.id)
            
        time_to_repair = update_field(filtering_function, data, 'timeToRepairValue', TimeToRepair)
        consequence_factor_data.time_to_repair = time_to_repair
            
        cost_of_repair = update_field(filtering_function, data, 'costOfRepairValue', CostOfRepair)
        consequence_factor_data.cost_of_repair = cost_of_repair
            
        probable_magnitude_of_product_loss = update_field(filtering_function, data, 'drainageMagnitudeValue', ProbableMagnitudeOfProductLoss)
        consequence_factor_data.probable_magnitude_of_product_loss = probable_magnitude_of_product_loss
            
        likelihood_of_injury_to_personnel = update_field(filtering_function, data, 'likelihoodOfInjuryValue', LikelihoodOfInjuryToPersonnel)
        consequence_factor_data.likelihood_of_injury_to_personnel = likelihood_of_injury_to_personnel
            
        product_flammability_as_per_MCSP = update_field(filtering_function, data, 'productFlamabilityValue', ProductFlammabilityAsPerMCSP)
        consequence_factor_data.product_flammability_as_per_MCSP = product_flammability_as_per_MCSP
        
        product_toxicity = update_field(filtering_function, data, 'productToxicityValue', ProductToxicity)
        consequence_factor_data.product_toxicity = product_toxicity
        
        location_of_tank_farm = update_field(filtering_function, data, 'locationOfTankValue', LocationOfTankFarm)
        consequence_factor_data.location_of_tank_farm = location_of_tank_farm
        
        environmetal_hazard = update_field(filtering_function, data, 'environHazardValue', EnvironmetalHazardToSoilAndWater)
        consequence_factor_data.environmetal_hazard_to_soil_and_water_as_the_potential_to_cause = environmetal_hazard
        
        vapour_emission = update_field(filtering_function, data, 'vapourEmissionValue', VapourEmission)
        consequence_factor_data.vapour_emission = vapour_emission
        
        consequence_factor_data.save()
        
        
        
        
        inspection_data = InspectionData.objects.get(id=proj.default_values.inspection_data.id)
        
        last_inspection = data['lastInspectionValue']
        inspection_data.last_inspection = datetime.strptime(last_inspection, '%Y-%m-%d').date()
    
        minimum_thickness_measured_during_previous_inspection = data['minThicknessMeasuredPrevInspValue']
        inspection_data.minimum_thickness_measured_during_previous_inspection = minimum_thickness_measured_during_previous_inspection
        
        period_of_service_between_previous_inspection_and_this_inspection = data['periodOfServiceBetweenPrevAndPresentInspeValue']
        inspection_data.period_of_service_between_previous_inspection_and_this_inspection = period_of_service_between_previous_inspection_and_this_inspection
        
        minimum_thickness_measured_during_present_inspection = data['minThicknessMeasuredPresentInspValue']
        inspection_data.minimum_thickness_measured_during_present_inspection = minimum_thickness_measured_during_present_inspection
    
        minimum_allowable_bottom_place_thickness = data['minAllowBottomPlaceThicknessValue']
        inspection_data.minimum_allowable_bottom_place_thickness = minimum_allowable_bottom_place_thickness
    
        acceleration_factor_for_pitting = update_field(filtering_function, data, 'accelerationFactorForPittingValue', AccelerationFactorForPitting)
        inspection_data.acceleration_factor_for_pitting = acceleration_factor_for_pitting
        
        NDT_method_used_for_thickness_measurements = update_field(filtering_function, data, 'ndtMethodUsedValue', NDTMethodUsedForThicknessMeasurements)
        inspection_data.NDT_method_used_for_thickness_measurements = NDT_method_used_for_thickness_measurements
        
        frequency_of_internal_inspections_performed_during_service_life = update_field(filtering_function, data, 'freqOfInternalInspValue', FrequencyOfInternalInspections)
        inspection_data.frequency_of_internal_inspections_performed_during_service_life = frequency_of_internal_inspections_performed_during_service_life
        
        type_of_interconnecting_bottom_plate_welds_outside_of_annular_section = update_field(filtering_function, data, 'typeOfInternectingValue', TypeOfInterconnectingBottomPlateWelds)
        inspection_data.type_of_interconnecting_bottom_plate_welds_outside_of_annular_section = type_of_interconnecting_bottom_plate_welds_outside_of_annular_section
        
        inspection_data.save()
        
        
        
        
        results = Results.objects.get(id=proj.default_values.results.id)
        print(results)
        
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
    