from django.conf import settings
from django.db import models

class Profesor(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_profesor')
    especialidad = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)