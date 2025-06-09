from django.conf import settings
from django.db import models


class Alumno(models.Model):
    """
    Modelo que representa a un alumno.
    """
    
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='alumno')
    codigo = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)

    # class Meta:
    #     verbose_name = "Alumno"
    #     verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
