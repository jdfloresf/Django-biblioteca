from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Prestamo
from .forms import PrestamoForm, PrestamoMultipleForm

# Create your views here.

class RegistrarPrestamo(FormView):
    template_name = 'prestamo/prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        # Metodo 1 para guardar datos en la DB con el ORM de django
        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestamo = date.today(),
        #     devuelto = False
        # )

        # Metodo 2
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()
        libro = form.cleaned_data['libro']
        libro.stok -= 1
        libro.save()


        return super(RegistrarPrestamo, self).form_valid(form)

class AddPrestamo(FormView):
    template_name = 'prestamo/prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False,
            defaults = {
                'fecha_prestamo': date.today()
            }
        )

        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            HttpResponseRedirect('/')

class AddMultiplePrestamo(FormView):
    template_name = 'prestamo/prestamo_multiple.html'
    form_class = PrestamoMultipleForm
    success_url = '.'

    def form_valid(self, form):

        prestamos = []

        for l in form.cleaned_data['libro']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto = False,
            )
            prestamos.append(prestamo)

        Prestamo.objects.bulk_create(
            prestamos
        )

        return super(AddPrestamo, self).form_valid(form)
