from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return f'{self.nombre} {self.apellido} '


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField(verbose_name='Stock en deposito', help_text='Ingresar cantidad neta en deposito')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
