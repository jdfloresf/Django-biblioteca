from django.db import models
from django.db.models.signals import post_delete

from apps.libro.models import Libro
from apps.autor.models import Persona

from .managers import PrestamoManager

# Create your models here.

class Lector(Persona):
    """Model definition for Lector."""
    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    """Model definition for Prestamo."""

    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestado')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def save(self, *args, **kwargs):
        self.libro.stok -= 1
        self.save()
        super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of Prestamo."""
        return self.lector.nombres + '-' + str(self.libro)
    
def upadte_libro_stok(sender, insance, **kwargs):
    insance.libro.stok += 1
    insance.libro.save()

post_delete.connect(upadte_libro_stok, sender=Prestamo)
