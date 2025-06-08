from django.db import models


class Alumno(models.Model):
    """
    Modelo que representa a un alumno.
    """
    
    ci = models.CharField(max_length=20, unique=True, verbose_name="Cédula de Identidad")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    genero = models.CharField(max_length=10,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro')
        ],
        default='O',
        verbose_name="Género"
    )
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    # class Meta:
    #     verbose_name = "Alumno"
    #     verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
