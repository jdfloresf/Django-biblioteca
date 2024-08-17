from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Libro

# Create your views here.


class LibrosListView(ListView):
    template_name = "libro/lista.html"
    context_object_name = "lista_libros"

    def get_queryset(self):
        kw = self.request.GET.get('libro', '')
        #fecha1
        f1 = self.request.GET.get('fecha1', '')
        # fecha2
        f2 = self.request.GET.get('fecha2', '')

        if f1 and f2:
            return Libro.objects.listar_libros2(kw, f1, f2)
        else:
            return Libro.objects.listar_libros(kw)

class Libros2ListView(ListView):
    template_name = "libro/lista2.html"
    context_object_name = "lista_libros"

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria('1')
    


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"
    context_object_name = 'libro'

