from django.conf import settings
from django.db import models

class Director(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_director')
    area_gestion = models.CharField(max_length=100)