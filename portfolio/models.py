from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Item(models.Model):
    title = models.CharField(verbose_name=_("Título"), max_length=50)
    description = models.CharField(verbose_name=_("Descripción"), max_length=200)
    image = models.ImageField(verbose_name=_("Archivo de portada"), upload_to='media/portfolio')
    categories = models.ManyToManyField('category.Category', verbose_name=_("Categorías"))
    created = models.DateField(verbose_name=_("Creado"), auto_now_add=True)
    updated = models.DateField(verbose_name=_("Actualizado"), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created']

