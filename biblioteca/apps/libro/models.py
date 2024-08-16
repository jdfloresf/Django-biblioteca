from django.db import models

# apps
from apps.autor.models import Autor

# Create your models here.

class Categoria(models.Model):
    """Model definition for Categoria."""

    nombre = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre

class Libro(models.Model):
    """Model definition for Libro."""

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento', auto_now=False, auto_now_add=False)
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        """Unicode representation of Libro."""
        return self.titulo
