from django.db import models

from config.settings import STATIC_URL
from config.settings import MEDIA_URL
from core.integrante.choices import rol_choices
# Create your models here.
from core.semillero.models import Semillero


class Integrante(models.Model):

    nombres = models.CharField(max_length=255)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    rol=models.CharField(max_length=20, choices=rol_choices, default='Docente')
    semillero=models.ForeignKey(Semillero, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='integrantes/%Y/%m/%d', null=True, blank=True, default='/static/img/robot.png')

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Integrantes'
        verbose_name_plural = 'Integrantes'
        ordering = ['id']
