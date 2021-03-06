from datetime import datetime

from django.db import models
from django.urls import reverse

from core.materiales.models import Materiales


class CommonInfoClientes(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, primary_key=True, error_messages={
        'unique': 'El cliente con este número de cédula ya existe',
    })
    telefono_celular = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'


class ContratoClientes(CommonInfoClientes):
    fecha_contrato = models.DateTimeField(default=datetime.now())
    valor_contrato = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    instalado = models.BooleanField(default=False)

    class Meta:
        db_table = 'contrato-clientes'

    def get_absolute_url(self):
        return reverse('clientes:informacion-cliente-contrato', kwargs={"id": self.cedula})


class Clientes(CommonInfoClientes):
    fecha_de_instalacion = models.DateTimeField(default=datetime.now())
    email = models.EmailField(max_length=100)
    activo = models.BooleanField()

    class Meta(CommonInfoClientes.Meta):
        db_table = 'clientes'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def get_absolute_url(self):
        return reverse('clientes:informacion-cliente', kwargs={"id": self.cedula})


class OrdenesTrabajoClientes(models.Model):
    INSTALACION_NUEVA = 'IN'
    CAMBIO_DOMICILIO = 'CD'
    ARREGLO = 'AR'
    ADICIONALES = 'AD'
    REINSTALACIONES = 'RI'
    SUSPENCIONES_VOLUNTARIAS = 'SV'
    CORTES_DE_SERVICIO = 'CS'

    DESCRIPCION_ACTIVIDADES_CHOICES = [
        (INSTALACION_NUEVA, 'Instalacion nueva'),
        (CAMBIO_DOMICILIO, 'Cambio de domicilio'),
        (ARREGLO, 'ARREGLO'),
        (ADICIONALES, 'Adicionales'),
        (REINSTALACIONES, 'Reinstalaciones'),
        (SUSPENCIONES_VOLUNTARIAS, 'Suspencion voluntaria'),
        (CORTES_DE_SERVICIO, 'Cortes de Servicio')

    ]

    numero_orden = models.CharField(max_length=333)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    materiales = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    pago_materiales = models.BooleanField(default=False)
    cantidad = models.PositiveIntegerField(default=0)
    descripcion_actividad = models.CharField(max_length=2, choices=DESCRIPCION_ACTIVIDADES_CHOICES)
    fecha_trabajo = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'orden de trabajo'
        verbose_name_plural = 'ordenes de trabajo'
        db_table = 'ordenes de trabajo clientes'


class PagosMensualidadesClientes(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(default=datetime.now)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'pagos'
        db_table = 'pagos_mensualidades_clientes'
