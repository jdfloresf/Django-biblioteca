from django.db import models

# Manager
from .managers import AutorManager
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    objects = AutorManager()

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self) -> str:
        return self.nombre + '-' + self.apellidos