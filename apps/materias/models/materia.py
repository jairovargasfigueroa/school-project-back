from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    curso = models.ForeignKey('cursos.Curso', on_delete=models.CASCADE, related_name='materias')
    docente = models.ForeignKey('usuarios.Profesor', on_delete=models.SET_NULL, null=True, blank=True, related_name='materias')
    gestion = models.ForeignKey('gestiones.Gestion', on_delete=models.CASCADE, related_name='materias', null=True, blank=True)

    def __str__(self):
        return self.nombre

