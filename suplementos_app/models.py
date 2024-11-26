from django.db import models

# Create your models here.

class Suplemento (models.Model):
    id_producto = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    sabor = models.CharField(max_length=15)
    precio_uni = models.IntegerField()
    peso = models.IntegerField()


    def __str__(self):
        return self.nombre