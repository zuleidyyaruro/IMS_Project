from django.db import models

from core.publicacion.choices import tipoPublicacion_choices

class Publicacion(models.Model):

    nombre=models.CharField(max_length=250)
    tipo_publicacion=models.CharField(max_length=30, choices=tipoPublicacion_choices, default='articulo')
    autores=models.CharField(max_length=255)
    anio_publicacion=models.CharField(max_length=5)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['id']