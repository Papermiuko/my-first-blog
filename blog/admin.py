from django.contrib import admin
from .models import Reserva

# En tu archivo admin.py

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha', 'hora', 'jornada', 'numero_personas')
