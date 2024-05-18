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



def reservar(request):
    if request.method == 'POST':
        # Procesar la reserva
        fecha_str = request.POST.get('fecha')
        fecha = datetime.strptime(fecha_str, '%d %b, %Y').strftime('%Y-%m-%d')

        nombre = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('phone')
        
        # Obtener la hora del formulario (en formato de 24 horas)
        hora_str = request.POST.get('hora')
        
        # Obtener el número de personas del formulario
        numero_personas = request.POST.get('person')

         # Obtener el número jornada del formulario
        jornada = request.POST.get('jornada')

        # Crear una instancia de Reserva
        reserva = Reserva(nombre=nombre, email=email, telefono=telefono, fecha=fecha, hora=hora_str, numero_personas=numero_personas, jornada=jornada)

        # Guardar la reserva
        reserva.save()

        # Agregar un mensaje de éxito
        messages.success(request, '¡Reserva realizada con éxito!')

        # Redirigir al usuario a la misma página de reserva
        return redirect('reservar')
    else:
        return render(request, 'reservation.html')
