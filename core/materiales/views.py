from django.shortcuts import render

from core.materiales.forms import MaterialesForm
from core.materiales.models import Materiales


# Create your views here.

def creacion_material(request):
    form = MaterialesForm
    lista_materiales = Materiales.objects.all()
    if request.method == 'POST':
        form = MaterialesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'Materiales/materiales-creado.html',{'img_obj': img_obj})
    return render(request, 'Materiales/materiales-form.html', {'form': form, 'lista_materiales': lista_materiales})
