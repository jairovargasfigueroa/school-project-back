from django.db import models

class Curso(models.Model):
    """
    Modelo que representa un curso.
    """

    class Nivel(models.TextChoices):
        INICIAL = 'inicial', 'Inicial'
        PRIMARIA = 'primaria', 'Primaria'
        SECUNDARIA = 'secundaria', 'Secundaria'

    class Turno(models.TextChoices):
        MAÑANA = 'mañana', 'Mañana'
        TARDE = 'tarde', 'Tarde'
        NOCHE = 'noche', 'Noche'
        
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.CharField(max_length=20, choices=Nivel.choices, default=Nivel.PRIMARIA)
    turno = models.CharField(max_length=20, choices=Turno.choices, default=Turno.MAÑANA)

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()}) - {self.get_turno_display()}"

    # class Meta:
    #     verbose_name = "Curso"
    #     verbose_name_plural = "Cursos"
    #     ordering = ['nombre']