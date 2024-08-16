from django.shortcuts import render
from django.views.generic import ListView

# Models
from .models import Autor

# Create your views here.


class AutorListView(ListView):
    template_name = "autor/autores.html"
    context_object_name = 'lista_autores'

    def get_queryset(self):
        kw = self.request.GET.get('autor', '')
        return Autor.objects.buscar_autor4(kw)



