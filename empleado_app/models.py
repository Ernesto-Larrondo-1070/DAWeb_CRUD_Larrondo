from django.db import models

class Empleado(models.Model):
    id_empleado = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rfc = models.CharField(max_length=15)
    curp = models.CharField(max_length=18)
    num_tel = models.CharField(max_length=12)
    dire = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 
