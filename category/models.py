from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = "categorías"
        ordering = ['name']
