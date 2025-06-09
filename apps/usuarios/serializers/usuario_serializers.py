from rest_framework import serializers
from apps.usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'rol', 'ci', 'telefono', 'genero', 'estado'
        ]
        exclude = ['password']