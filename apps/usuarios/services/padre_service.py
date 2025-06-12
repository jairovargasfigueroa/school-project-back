from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.usuarios.models import Padre
from apps.usuarios.services.usuario_service import UsuarioService

class PadreService:

    @staticmethod
    @transaction.atomic
    def crear_padre(data: dict) -> Padre:
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

        usuario = UsuarioService.crear_usuario(datos_usuario)
        padre = Padre.objects.create(usuario=usuario, **data)
        return padre

    @staticmethod
    @transaction.atomic
    def actualizar_padre(padre_id, data):
        padre = get_object_or_404(Padre, id=padre_id)
        usuario = padre.usuario

        campos_usuario = ['username', 'email', 'first_name', 'last_name', 'rol', 'ci', 'telefono', 'genero', 'estado']
        for field in campos_usuario:
            setattr(usuario, field, data[field])

        if "password" in data and data["password"]:
            usuario.set_password(data["password"])

        usuario.save()

        campos_padre = ['ocupacion']
        for field in campos_padre:
            setattr(padre, field, data[field])
        padre.save()


        return padre

    @staticmethod
    def eliminar_padre(padre_id):
        padre = Padre.objects.filter(id=padre_id).first()
        if padre:
            padre.usuario.delete()
            padre.delete()
            return True
        return False

    @staticmethod
    def obtener_padre_por_id(padre_id):
        return get_object_or_404(Padre, id=padre_id)