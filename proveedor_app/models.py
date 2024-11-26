from django.db import models

# Create your models here.
class Proveedor (models.Model):
    id_provee = models.PositiveSmallIntegerField(primary_key=True)
    num_ruta = models.CharField(max_length=10)
    cant_prod = models.IntegerField()
    peso = models.FloatField()
    tipo_prod = models.CharField(max_length=30)
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return self.num_ruta