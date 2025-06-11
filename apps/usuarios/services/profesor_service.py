# services/profesor_service.py
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.usuarios.models import Profesor  
from apps.usuarios.services.usuario_service import UsuarioService

class ProfesorService:

    @staticmethod
    @transaction.atomic
    def crear_profesor(data: dict) -> Profesor:
        datos_usuario = {key: data.pop(key) for key in [
            'username', 'password', 'email', 'first_name', 'last_name', 'rol',
            'ci', 'telefono', 'genero', 'estado'
        ]}
        usuario = UsuarioService.crear_usuario(datos_usuario)
        return Profesor.objects.create(usuario=usuario, **data)

    @staticmethod
    def listar_profesores():
        return Profesor.objects.select_related('usuario').all()

    @staticmethod
    def obtener_profesor_por_id(pk: int):
        return Profesor.objects.filter(id=pk).first()

    @staticmethod
    @transaction.atomic
    def actualizar_profesor(pk: int, data: dict):
        profesor = get_object_or_404(Profesor, id=pk)
        usuario = profesor.usuario

        for field in ['username', 'email', 'first_name', 'last_name', 'rol', 'ci', 'telefono', 'genero', 'estado']:
            setattr(usuario, field, data[field])
        usuario.save()

        profesor.especialidad = data['especialidad']
        profesor.save()
        return profesor

    @staticmethod
    @transaction.atomic
    def eliminar_profesor(pk: int):
        profesor = Profesor.objects.filter(id=pk).first()
        if profesor:
            profesor.usuario.delete()
            profesor.delete()
            return True
        return False