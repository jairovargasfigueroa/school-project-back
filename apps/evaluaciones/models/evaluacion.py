from email.policy import default
from django.db import models

class Evaluacion(models.Model):
    TIPO_CHOICES = [
        ('examen', 'Examen'),
        ('tarea', 'Tarea'),
        ('participacion', 'Participación'),
        ('otro', 'Otro'),
    ]
    
    DIMENSIONES = [
        ("ser", "Ser"),
        ("saber", "Saber"),
        ("hacer", "Hacer"),
        ("decidir", "Decidir"),
    ]

    TRIMESTRES = [
        (1, "Primer Trimestre"),
        (2, "Segundo Trimestre"),
        (3, "Tercer Trimestre"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    dimension = models.CharField(max_length=20, choices=DIMENSIONES, default="saber")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 20.00
    trimestre = models.IntegerField( choices=TRIMESTRES, default=1)
    materia = models.ForeignKey('materias.Materia', on_delete=models.CASCADE, related_name='evaluaciones')
    gestion = models.ForeignKey('gestiones.Gestion', on_delete=models.CASCADE, related_name='evaluaciones')

    def __str__(self):
        return f"{self.nombre} - {self.materia.nombre} ({self.tipo})"
