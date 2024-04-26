from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import rest_framework as filters
from .filter import MotherFilter
from .models import Mother, Mother_visit
from .serializers import MotherSerializer, MotherVisitSerializer

# Create your views here.

class MotherViewSet(viewsets.ModelViewSet):
    queryset= Mother.objects.all()
    serializer_class=MotherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MotherFilter
    # filterset_fields = ['healthcare_centre_name','mother_name','registration_number','mosquito_net_voucher_number','mother_age','mother_education','mother_employment','Height','partner_name','partner_age','partner_work','partner_education','address','Chairperson_name','pregnancies','alive_children','miscarrimother_ages','births','miscarrimother_age_year','miscarrimother_age_mother_age']

    #permission_classes=[permissions.IsAuthenticated]


class MotherVisitViewSet(viewsets.ModelViewSet):
    queryset= Mother_visit.objects.all()
    serializer_class=MotherVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]

    