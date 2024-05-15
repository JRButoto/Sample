from django_filters import rest_framework as filters
from .models import Mother


class MotherFilter(filters.FilterSet):
    mother_age_gt = filters.NumberFilter(field_name="mother_age", lookup_expr='gte')
    mother_age_lt = filters.NumberFilter(field_name="mother_age", lookup_expr='lte')
    mother_name = filters.CharFilter(field_name="mother_name", lookup_expr='icontains')

    class Meta:
        model = Mother
        fields = ['mother_age', 'mother_name']