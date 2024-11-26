from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta = models.PositiveSmallIntegerField(primary_key=True)
    id_prod = models.PositiveSmallIntegerField()
    cliente = models.CharField(max_length=10)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    gr_kg = models.CharField(max_length=10)
    servicios = models.CharField(max_length=100)

    def __str__(self):
        return self.cliente