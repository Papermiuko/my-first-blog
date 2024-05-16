from django.urls import path
from . import views
from .views import reservar

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('gallery.html', views.gallery, name='gallery'),
    path('menu.html', views.menu, name='menu'),
    path('reservation.html', views.reservation, name='reservation'),
    path('reservar/', reservar, name='reservar'),
]