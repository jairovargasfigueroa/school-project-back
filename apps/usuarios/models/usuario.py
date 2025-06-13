from django.contrib.auth.models import AbstractUser
from django.db import models

#Modelo de usuario en ue definimos el rol y campos adicionales que tendran todos lo usuarios
#Usamos AbstractUser para heredar los campos básicos de usuario de Django
#Y aprovechamos todo lo que nos ofrece Django para la autenticación y gestión de usuarios. 
class Usuario(AbstractUser):
    """
    Modelo que representa a un usuario del sistema.
    Hereda de AbstractUser para incluir campos adicionales si es necesario.
    """
    
    # Puedes agregar campos adicionales aquí si es necesario
    # Por ejemplo, un campo de perfil o preferencias del usuario
    
    username = models.CharField(max_length=150, unique=True)

    class Rol(models.TextChoices):
        ALUMNO = 'alumno'
        PROFESOR = 'profesor'
        DIRECTOR = 'director'
        PADRE = 'padre'
    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.ALUMNO,
        verbose_name="Rol del Usuario"
    )
    ci = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    genero = models.CharField(max_length=10,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro')
        ],
        default='O',
        verbose_name="Género"
    )
    estado = models.CharField(max_length=15)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username  # O cualquier otro campo que desees mostrar