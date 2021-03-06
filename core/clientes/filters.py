import django_filters
from django_filters import CharFilter

from core.clientes.models import *


class ClienteFilters(django_filters.FilterSet):
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Apellido')
    address = CharFilter(field_name='address', lookup_expr='icontains', label='Dirección')

    class Meta:
        model = Clientes
        fields = '__all__'
        exclude = ['telefono_celular', 'email', 'first_name', 'fecha_de_instalacion']
