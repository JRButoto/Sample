from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filter import MotherFilter
from .models import Mother, Mother_visit
from .serializers import MotherSerializer, MotherVisitSerializer

# Create your views here.

class MotherViewSet(viewsets.ModelViewSet):
    queryset= Mother.objects.all()
    serializer_class=MotherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MotherFilter
    #permission_classes=[permissions.IsAuthenticated]


class MotherVisitViewSet(viewsets.ModelViewSet):
    queryset= Mother_visit.objects.all()
    serializer_class=MotherVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]


@api_view(['GET'])
def getMotherSummary(request):
    mother_data = Mother.objects.values('mother_name', 'mother_age')
    
    # Extract weight and height from Child_visit objects
    mother_visits_data = Mother_visit.objects.values('visit_number', 'visit_date')

    # Convert the querysets to lists
    mother_data_list = list(mother_data)
    mother_visits_data_list = list(mother_visits_data)
    
    # Construct the response data
    response_data = {
        'children': mother_data_list,
        'children_visits': mother_visits_data_list
    }

    return Response(response_data)

    