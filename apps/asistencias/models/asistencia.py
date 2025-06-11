from django.db import models

class Asistencia(models.Model):
    alumno = models.ForeignKey('usuarios.Alumno', on_delete=models.CASCADE, related_name='asistencias')
    materia = models.ForeignKey('materias.Materia', on_delete=models.CASCADE, related_name='asistencias')
    gestion = models.ForeignKey('gestiones.Gestion', on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField()
    presente = models.BooleanField()

    class Meta:
        unique_together = ('alumno', 'materia', 'gestion', 'fecha')
        ordering = ['fecha']

    def __str__(self):
        return f"{self.fecha} - {self.alumno} - {self.materia}: {'Presente' if self.presente else 'Falta'}"
