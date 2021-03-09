from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core.clientes.filters import ClienteFilters
from core.clientes.forms import BusquedaForm, ContratoForm, ClientesForm, OrdenesTrabajoClientesForm
from core.clientes.models import ContratoClientes, Clientes, OrdenesTrabajoClientes


def dashboard(request):
    clientes = Clientes.objects.all()
    context = {'clientes': clientes}
    return render(request, 'home.html', context)


def busqueda_clientes(request):
    my_form = BusquedaForm
    busqueda = request.GET.get('busqueda')
    if request.method == "GET":
        my_form = BusquedaForm(request.GET)
        if len(str(busqueda)) == 10:
            try:
                cliente = Clientes.objects.get(cedula=busqueda)

            except Clientes.DoesNotExist:
                cliente = "No existe el cliente."
            return render(request, 'Clientes/search-cliente.html',
                          {'cliente': cliente, 'form': my_form})
        elif busqueda:
            clientes = Clientes.objects.filter(last_name__icontains=busqueda)
            return render(request, 'Clientes/search-cliente.html', {'clientes': clientes, 'form': my_form})
    return render(request, 'Clientes/search-cliente.html', {'form': my_form})


def busqueda_contratos_clientes(request):
    form = BusquedaForm
    busqueda = request.GET.get('busqueda')
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if len(str(busqueda)) == 10:
            try:
                cliente = ContratoClientes.objects.get(cedula=busqueda, instalado=False)
            except ContratoClientes.DoesNotExist:
                cliente = 'El Cliente ya se encuentra instalado'
            return render(request, 'Clientes/search-contrato.html', {'form': form, 'cliente': cliente})
        elif busqueda:
            clientes_contrato = ContratoClientes.objects.filter(last_name__icontains=busqueda, instalado=False)
            return render(request, 'Clientes/search-contrato.html',
                          {'clientes_contrato': clientes_contrato, 'form': form})
    return render(request, 'Clientes/search-contrato.html', {'form': form})


def cliente_contrato_info(request, id):
    cliente_contrato = ContratoClientes.objects.get(cedula=id)
    return render(request, 'Clientes/info-contrato-clientes.html', {'cliente': cliente_contrato})


def contrato_nuevo(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('exito/')
    else:
        form = ContratoForm()
    return render(request, "Clientes/contrato_clientes.html", {'form': form})


def activar_cliente(request, id):
    contrato_cliente = ContratoClientes.objects.get(cedula=id)
    if request.method == "POST":
        form = ClientesForm(request.POST)
        contrato_cliente = ContratoClientes.objects.get(cedula=id)

        if form.is_valid():
            contrato_cliente.instalado = True
            contrato_cliente.save()
            form.save()
            cedula = contrato_cliente.cedula
            return HttpResponseRedirect(reverse('clientes:materiales-activacion', kwargs={"id": cedula}))
    else:
        contrato_cliente = ContratoClientes.objects.get(cedula=id)
        if not contrato_cliente.instalado:
            data = {
                'first_name': contrato_cliente.first_name,
                'last_name': contrato_cliente.last_name,
                'cedula': contrato_cliente.cedula,
                'address': contrato_cliente.address,
                'telefono_celular': contrato_cliente.telefono_celular
            }
            form = ClientesForm(initial=data)
            return render(request, 'Clientes/activar_cliente.html',
                          {'form': form, })
        else:
            mensaje = 'El Cliente se encuentra instalado'
            return render(request, 'Clientes/activar_cliente.html', {'mensaje': mensaje})

    return render(request, 'Clientes/activar_cliente.html', {'form': form, })


def materiales_despues_activacion_cliente(request, id):
    instancia = Clientes.objects.get(cedula=id)
    form = OrdenesTrabajoClientesForm(instance=instancia, prefix='orden_trabajo')
    MaterialFormSet = inlineformset_factory(Clientes,
                                            OrdenesTrabajoClientes,
                                            fields=('materiales', 'cantidad',
                                                    # 'numero_orden',
                                                    # 'descripcion_actividad'
                                                    ),

                                            extra=3,
                                            # widgets={'numero_orden': forms.HiddenInput(),
                                            #          'descripcion_actividad': forms.HiddenInput()
                                            #          },
                                            can_delete=False,
                                            )
    formset = MaterialFormSet(
        #
        # initial=[
        #     {'numero_orden': 'None', 'descripcion_actividad': 'IN'},
        #     {'numero_orden': 'None', 'descripcion_actividad': 'IN'},
        #     {'numero_orden': 'None', 'descripcion_actividad': 'IN'},
        #     {'numero_orden': 'None', 'descripcion_actividad': 'IN'},
        # ],

    )
    if request.method == "POST":
        form = OrdenesTrabajoClientesForm(request.POST, instance=instancia, prefix='orden_trabajo')
        numero_orden = form.data.get('orden_trabajo-numero_orden')
        formset = MaterialFormSet(request.POST, instance=instancia)
        if formset.is_valid():
            instancia_form_set = formset.save(commit=False)
            for instance in instancia_form_set:
                instance.numero_orden = numero_orden
                instance.descripcion_actividad = 'IN'
                instance.save()

            return HttpResponseRedirect(instancia.get_absolute_url())
    cliente = Clientes.objects.get(cedula=id)
    return render(request, 'Clientes/activar_cliente_materiales.html',
                  {'form': form, 'formset': formset, 'cliente': cliente})


def informacion_cliente(request, id):
    cliente = Clientes.objects.get(cedula=id)
    cliente_contrato = ContratoClientes.objects.get(cedula=id)
    context = {'cliente': cliente, 'cliente_contrato': cliente_contrato}
    return render(request, 'Clientes/info-cliente.html', context)


def lista_clientes(request):
    clientes = Clientes.objects.all()
    myFilter = ClienteFilters(request.GET, queryset=clientes)
    clientes = myFilter.qs
    context = {'clientes': clientes, 'myFilter': myFilter}
    return render(request, 'Clientes/lista-clientes.html', context)
