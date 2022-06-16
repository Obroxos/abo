from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Proceso(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Autor",
    )
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo", blank=True)
    video = models.CharField(max_length=200, verbose_name="Video", blank=True)
    content = models.TextField(verbose_name="Contenido", blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="media", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proceso"
        verbose_name_plural = "procesos"
        ordering = ['-created']

    def __str__(self):
        return self.title

