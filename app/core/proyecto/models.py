from django.db import models

from core.semillero.models import Semillero


class Proyecto(models.Model):
    nombre=models.CharField(max_length=255)
    semillero=models.ForeignKey(Semillero, on_delete=models.CASCADE)
    autores=models.CharField(max_length=255)
    fecha_inicio=models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']