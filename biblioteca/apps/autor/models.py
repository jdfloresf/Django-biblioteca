from django.db import models

# Manager
from .managers import AutorManager
# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos
    
    class Meta:
        abstract = True

class Autor(Persona):
    seudonimo = models.CharField('seudonimo', max_length=50, blank=True)
    objects = AutorManager()

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    
