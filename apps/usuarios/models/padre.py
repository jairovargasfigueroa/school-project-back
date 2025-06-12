from django.conf import settings
from django.db import models

class Padre(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_padre'
    )
    ocupacion = models.CharField(max_length=100)
    direccion_trabajo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - Padre"
