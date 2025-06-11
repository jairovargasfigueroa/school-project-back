# from apps.usuarios.models import Alumno


# def crear_Alumno(alumno_data):
#     """
#     Crea un nuevo alumno con los datos proporcionados.
    
#     :param alumno_data: Diccionario con los datos del alumno.
#     :return: Instancia del alumno creado.
#     """
#     return Alumno.objects.create(**alumno_data)

# def actualizar_Alumno(alumno, alumno_data):
#     """
#     Actualiza un alumno existente con los nuevos datos proporcionados.
    
#     :param alumno: Instancia del alumno a actualizar.
#     :param alumno_data: Diccionario con los nuevos datos del alumno.
#     :return: Instancia del alumno actualizado.
#     """
#     for attr, value in alumno_data.items():
#         setattr(alumno, attr, value)
#     alumno.save()
#     return alumno

# def eliminar_Alumno(alumno):
#     """
#     Elimina un alumno existente.
    
#     :param alumno: Instancia del alumno a eliminar.
#     :return: None
#     """
#     alumno.delete()

# def obtener_Alumno_por_id(alumno_id):
#     """
#     Obtiene un alumno por su ID.
    
#     :param alumno_id: ID del alumno a buscar.
#     :return: Instancia del alumno encontrado o None si no existe.
#     """
#     try:
#         return Alumno.objects.get(id=alumno_id)
#     except Alumno.DoesNotExist:
#         return None       

    
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.usuarios.models import Alumno
from apps.usuarios.services.usuario_service import UsuarioService

class AlumnoService:

    @staticmethod
    @transaction.atomic
    def crear_alumno(data: dict) -> Alumno:
        if not data.get("password"):
            raise ValueError("El campo 'password' es obligatorio para crear un usuario.")

        datos_usuario = {
            'username': data.pop('username'),
            'password': data.pop('password'),
            'email': data.pop('email'),
            'first_name': data.pop('first_name'),
            'last_name': data.pop('last_name'),
            'rol': data.pop('rol'),
            'ci': data.pop('ci'),
            'telefono': data.pop('telefono'),
            'genero': data.pop('genero'),
            'estado': data.pop('estado'),
        }
        
        curso_id = data.pop('curso_id')  # <-- 🔥 ESTA LÍNEA
        usuario = UsuarioService.crear_usuario(datos_usuario)
        alumno = Alumno.objects.create(usuario=usuario,curso_id = curso_id, **data)
        
        return alumno

    @staticmethod
    @transaction.atomic
    def actualizar_alumno(alumno_id, data):
        alumno = get_object_or_404(Alumno, id=alumno_id)
        usuario = alumno.usuario

        campos_usuario = ['username', 'email', 'first_name', 'last_name', 'rol', 'ci', 'telefono', 'genero', 'estado']
        for field in campos_usuario:
            setattr(usuario, field, data[field])

        # Solo actualiza password si viene en la petición
        if "password" in data and data["password"]:
            usuario.set_password(data["password"])

        usuario.save()

        campos_alumno = ['codigo', 'fecha_nacimiento', 'direccion']
        for field in campos_alumno:
            setattr(alumno, field, data[field])
        alumno.save()

        return alumno

    @staticmethod
    def eliminar_alumno(alumno_id):
        alumno = Alumno.objects.filter(id=alumno_id).first()
        if alumno:
            alumno.usuario.delete()
            alumno.delete()
            return True
        return False
    
    @staticmethod
    def obtener_alumno_por_id(alumno_id: int):
        return Alumno.objects.filter(id=alumno_id).first()

    @staticmethod
    def listar_alumnos():
        return Alumno.objects.select_related('usuario').all()
    