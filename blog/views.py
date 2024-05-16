from django.shortcuts import render, redirect
from .models import Reserva
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def reservation(request):
    return render(request, 'reservation.html', {})

from django.contrib import messages
from .models import Reserva

def reservar(request):
    if request.method == 'POST':
        # Procesar la reserva
        fecha_str = request.POST.get('fecha')
        fecha = datetime.strptime(fecha_str, '%d %b, %Y').strftime('%Y-%m-%d')

        nombre = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('phone')
        hora = request.POST.get('hora')
        numero_personas = request.POST.get('person')

        # Crear una instancia de Reserva
        reserva = Reserva(nombre=nombre, email=email, telefono=telefono, fecha=fecha, hora=hora, numero_personas=numero_personas)

        # Guardar la reserva
        reserva.save()

        # Agregar un mensaje de éxito
        messages.success(request, '¡Reserva realizada con éxito!')

        # Redirigir al usuario a la misma página de reserva
        return redirect('reservar')
    else:
        return render(request, 'reservation.html')


