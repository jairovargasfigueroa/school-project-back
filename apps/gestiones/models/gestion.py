from django.db import models

class Gestion(models.Model):
    anio = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=100, blank=True)
    activa = models.BooleanField(default=False)

    class Meta:
        ordering = ['-anio']

    def __str__(self):
        return f"Gestión {self.anio}"
