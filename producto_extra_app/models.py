from django.db import models

# Create your models here.

class Producto_extra (models.Model):
    id_prod = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    talla = models.CharField(max_length=15)
    precio_uni = models.IntegerField()
    peso = models.IntegerField()
    id_proveedor = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.nombre