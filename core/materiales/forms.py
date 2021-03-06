from django.forms import ModelForm

from core.materiales.models import Materiales


class MaterialesForm(ModelForm):
    class Meta:
        model = Materiales
        fields = ['codigo', 'nombre_producto', 'marca', 'imagen', ]
