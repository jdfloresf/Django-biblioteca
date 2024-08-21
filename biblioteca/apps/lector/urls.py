from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prestamo/', views.RegistrarPrestamo.as_view(), name='prestamo_registro'),
    path('prestamo/', views.RegistrarPrestamo.as_view(), name='prestamo_registro'),
    path('prestamo-mult/', views.AddMultiplePrestamo.as_view(), name='prestamo-mult_registro'),
]
