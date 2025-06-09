from django.db import models

class Curso(models.Model):
    NIVELES = [
        ('Inicial', 'Inicial'),
        ('Primario', 'Primario'),
        ('Secundario', 'Secundario'),
    ]

    TURNOS = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]

    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVELES)
    turno = models.CharField(max_length=20, choices=TURNOS)
    gestion = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.gestion}'
    
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    #docente_id = models.ForeigKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'
