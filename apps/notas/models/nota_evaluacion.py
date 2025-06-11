from django.db import models

class NotaEvaluacion(models.Model):
    evaluacion = models.ForeignKey('evaluaciones.Evaluacion', on_delete=models.CASCADE, related_name='notas')
    alumno = models.ForeignKey('usuarios.Alumno', on_delete=models.CASCADE, related_name='notas_evaluacion')
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('evaluacion', 'alumno')  # Solo una nota por alumno y evaluación

    def __str__(self):
        return f"{self.alumno} - {self.evaluacion}: {self.nota}"

