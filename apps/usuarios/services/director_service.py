# apps/usuarios/services/director_service.py
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.usuarios.models import Director  
from apps.usuarios.services.usuario_service import UsuarioService

class DirectorService:

    @staticmethod
    @transaction.atomic
    def crear_director(data: dict) -> Director:
        usuario_data = {k: data.pop(k) for k in [
            'username', 'password', 'email', 'first_name', 'last_name',
            'rol', 'ci', 'telefono', 'genero', 'estado'
        ]}
        usuario = UsuarioService.crear_usuario(usuario_data)
        return Director.objects.create(usuario=usuario, **data)

    @staticmethod
    def listar_directores():
        return Director.objects.select_related('usuario').all()

    @staticmethod
    def obtener_director_por_id(pk: int):
        return Director.objects.filter(id=pk).first()

    @staticmethod
    @transaction.atomic
    def actualizar_director(pk: int, data: dict):
        director = get_object_or_404(Director, id=pk)
        usuario = director.usuario

        for field in ['username', 'email', 'first_name', 'last_name', 'rol', 'ci', 'telefono', 'genero', 'estado']:
            setattr(usuario, field, data[field])
        usuario.save()

        director.area_gestion = data['area_gestion']
        director.save()
        return director

    @staticmethod
    @transaction.atomic
    def eliminar_director(pk: int):
        director = Director.objects.filter(id=pk).first()
        if director:
            director.usuario.delete()
            director.delete()
            return True
        return False
