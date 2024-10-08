from django.db import models
from django.db.models.signals import post_save

from PIL import Image

# apps
from apps.autor.models import Autor
from .managers import LibroManager, CategoriaManager

# Create your models here.

class Categoria(models.Model):
    """Model definition for Categoria."""

    nombre = models.CharField(max_length=50)
    objects = CategoriaManager()

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return str(self.id) + '-' + self.nombre

class Libro(models.Model):
    """Model definition for Libro."""

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento', auto_now=False, auto_now_add=False)
    portada = models.ImageField(upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        """Unicode representation of Libro."""
        return str(self.id) + '-' + self.titulo


def optimize_image(sender, instance, **kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)



post_save.connect(optimize_image, sender=Libro)
