from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(default=timezone.now)
    plan = models.ForeignKey('plan', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=15, decimal_places=3)
    duracion_meses = models.IntegerField()

    def __str__(self):
        return self.nombre

    


