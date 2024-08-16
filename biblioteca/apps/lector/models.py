from django.db import models
from apps.libro.models import Libro

# Create your models here.

class Lector(models.Model):
    """Model definition for Lector."""

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        """Unicode representation of Lector."""
        return self.nombres
    
class Prestamo(models.Model):
    """Model definition for Prestamo."""

    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()



    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        """Unicode representation of Prestamo."""
        return self.lector + '-' + self.libro