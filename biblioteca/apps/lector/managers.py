from django.db import models
from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower 

class PrestamoManager(models.Manager):
    def libros_promedio_edades(self):
        result = self.filter(
            libro__id='1'
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edades = Sum('lector__edad')
        )
        return result

    def num_libros_prestados(self):
        result = self.values(
            'libro',
            'lector'
        ).annotate(
            num = Count('libro'),
            titulo = Lower('libro__titulo'),
            nombre = Lower('lector__nombres')

        )
        return result
