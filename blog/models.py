from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    numero_personas = models.IntegerField()

    def __str__(self):
        return self.nombre
