from django import forms
from django.forms import inlineformset_factory

from core.clientes.models import ContratoClientes, Clientes, OrdenesTrabajoClientes


class ContratoForm(forms.ModelForm):
    class Meta:
        model = ContratoClientes
        fields = ['first_name', 'last_name', 'cedula', 'telefono_celular', 'address', 'valor_contrato', ]
        labels = {
            'first_name': "Nombres",
            'last_name': 'Apellidos',
            'cedula': 'Cédula',
            'telefono_celular': 'Teléfono Celular',
            'address': 'Dirección',
            'valor_contrato': 'Precio del contrato'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'test'})
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if len(cedula) != 10:
            raise forms.ValidationError('La cedula debe contener 10 digitos')
        return cedula

    def clean_telefono_celular(self):
        numeros = '0123456789'
        celular = self.cleaned_data.get('telefono_celular')
        for numero in celular:
            if numero not in numeros:
                raise forms.ValidationError('Solo debe contener numeros')
        return celular


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)

    def clean_busqueda(self):
        busqueda_cliente = self.cleaned_data.get('busqueda')
        if len(busqueda_cliente) == 0:
            raise forms.ValidationError('No ha ingresado ninguna consulta')
        return busqueda_cliente


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['first_name', 'last_name', 'cedula', 'telefono_celular', 'address', 'fecha_de_instalacion', 'activo']
        labels = {
            'first_name': "Nombres",
            'last_name': 'Apellidos',
            'cedula': 'Cédula',
            'telefono_celular': 'Teléfono Celular',
            'address': 'Dirección',
            'valor_contrato': 'Precio del contrato'
        }


class OrdenesTrabajoClientesForm(forms.ModelForm):
    class Meta:
        model = OrdenesTrabajoClientes
        fields = ['numero_orden']



