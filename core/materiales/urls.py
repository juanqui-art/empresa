from django.urls import path
from django.views.generic import TemplateView

from core.materiales.views import creacion_material

app_name = 'materiales'
urlpatterns = [
    path('creacion_materiales/', creacion_material, name='creacion-material'),
    path('materiales-home/', TemplateView.as_view(template_name='Materiales/materiales-home.html'),
         name='home-materiales')
]
