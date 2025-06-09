from apps.usuarios.models import Usuario

class UsuarioService:

    @staticmethod
    def crear_usuario(data: dict) -> Usuario:
        """
        Crea un usuario utilizando `create_user` para hashear la contraseña.
        """
        return Usuario.objects.create_user(**data)

    @staticmethod
    def obtener_usuario_por_id(user_id: int):
        return Usuario.objects.filter(id=user_id).first()
