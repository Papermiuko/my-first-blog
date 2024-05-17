from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    jornada = models.CharField(
        max_length=2,
        choices=[('AM', 'AM'), ('PM', 'PM')],
        default='AM'
    )
    numero_personas = models.IntegerField()

    def __str__(self):
        # Formatear la hora para mostrarla en el formato deseado (con AM/PM)
        hora_formatted = self.hora.strftime('%I:%M')
        return f'{self.nombre} - {hora_formatted} {self.jornada}'
