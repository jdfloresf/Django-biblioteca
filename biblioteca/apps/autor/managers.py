from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """manager para el modelo autor"""

    def buscar_autor(self, kword):
        result = self.filter(
            nombre__icontains=kword
        )
        return result
    
    def buscar_autor2(self, kword):
        result = self.filter(
            # Filtrar busqueda para obtener un autor por coincidencias entre
            # el nombre o apellidos
           Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return result
    
    def buscar_autor3(self, kword ):
        result = self.filter(
            nombre__icontains=kword
        ).filter(Q(edad__icontains=52) | Q(edad__icontains=61))
        return result
    
    def buscar_autor4(self, kword):
        result = self.filter(
            edad__gt=40,
            edad__lt=70
        ).order_by('nombre', 'apellidos')
        return result