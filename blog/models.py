from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name=_('Título'), max_length=100)
    content = RichTextUploadingField()
    image = models.ImageField(verbose_name=_('Imagen'), upload_to="blog")
    author = models.ForeignKey("members.Member", verbose_name=_("Autor"), on_delete=models.CASCADE)
    categories = models.ManyToManyField("category.Category", verbose_name=_("Categorías"))
    created = models.DateField(verbose_name=_("Creado"), auto_now_add=True)
    updated = models.DateField(verbose_name=_("Actualizado"), auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
