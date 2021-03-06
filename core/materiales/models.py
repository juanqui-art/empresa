from django.db import models


class Materiales(models.Model):
    nombre_producto = models.CharField(max_length=100, blank=False)
    marca = models.CharField(max_length=99)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now=True)
    codigo = models.CharField(max_length=100, blank=True, unique=True)
    imagen = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiales'
        db_table = 'materiales' 

    def __str__(self):
        return f"{self.nombre_producto}"


class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=99)
    ruc = models.CharField(max_length=99)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=99)
    email = models.EmailField(max_length=99)
    creacion_proveedor = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = "Proveedores"
        db_table = 'proveedores'

    def __str__(self):
        return f"{self.nombre_proveedor}"


class OrdenesCompraMateriales(models.Model):
    nombre_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=333)
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=0)
    codigo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'orden de compra'
        verbose_name_plural = 'ondenes de compras'
        db_table = 'ordenes_de_compras'

# class Inventario(models.Model):
#     item = models.ForeignKey(Materiales, on_delete=models.CASCADE)
#
#     cantidad = models.PositiveBigIntegerField(default=0)
