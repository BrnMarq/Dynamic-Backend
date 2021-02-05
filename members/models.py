from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Member(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length=50)
    description = models.CharField(verbose_name=_("Descripción"), max_length=200)
    image = models.ImageField(verbose_name=_("Imagen"), upload_to="members")

    class Meta:
        ordering = ['name']
        verbose_name = "miembro"
        verbose_name_plural = "miembros"

    def __str__(self):
        return self.name

    
    