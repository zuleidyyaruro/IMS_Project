from django.db import models

# Create your models here.
class Semillero(models.Model):

    nombre = models.CharField(max_length=50)
    linea_investigacion = models.CharField(max_length=70)
    anio_constitucion = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    correo = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Semillero'
        verbose_name_plural = 'Semilleros'
        ordering = ['id']