import datetime

from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    """manager para el modelo autor"""

    def listar_libros(self, kword):
        result = self.filter(
            titulo__icontains=kword,
            fecha__range=('1900-01-1', '2000-01-01')
        )
        return result
   
    def listar_libros2(self, kword, fecha1, fecha2):
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()

        result = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return result
  
    def listar_libros_categoria(self, categoria):
        return self.filter(categoria__id=categoria).order_by('titulo')
    
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    

class CategoriaManager(models.Manager):

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()