from django.urls import path
from django.views.generic import TemplateView

from core.clientes.views import (busqueda_clientes,
                                 cliente_contrato_info,
                                 contrato_nuevo,
                                 busqueda_contratos_clientes,
                                 activar_cliente,
                                 informacion_cliente,
                                 materiales_despues_activacion_cliente,
                                 lista_clientes,
                                 # dashboard,
                                 )

app_name = 'clientes'
urlpatterns = [
    # path('dashboard/', dashboard, name='dashboard'),
    path('busqueda_clientes/', busqueda_clientes, name='busqueda-clientes'),
    path('informacion_cliente/<str:id>/', informacion_cliente, name='informacion-cliente'),
    path('busqueda_contratos_clientes', busqueda_contratos_clientes, name='busqueda-contratos-clientes'),
    path('informacion_cliente_contrato/<str:id>/', cliente_contrato_info, name='informacion-cliente-contrato'),
    path('activar_cliente/<str:id>/', activar_cliente, name='activar-cliente'),
    path('contrato_nuevo/', contrato_nuevo, name='contrato-nuevo'),
    path('contrato_nuevo/exito/', TemplateView.as_view(template_name='Clientes/contrato-cliente-exito.html'), name='creado-exito'),
    path('activar_cliente_material/<str:id>', materiales_despues_activacion_cliente, name='materiales-activacion'),
    path('lista_clientes/', lista_clientes, name='lista-clientes'),
    path('pagos_home/', TemplateView.as_view(template_name='Clientes/pagos-home.html'), name='pagos-home')

]
