# serializers/profesor_serializers.py
from rest_framework import serializers
from apps.usuarios.models import  Profesor, Usuario

class ProfesorWriteSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    rol = serializers.ChoiceField(choices=Usuario.Rol.choices)
    ci = serializers.CharField()
    telefono = serializers.CharField()
    genero = serializers.CharField()
    estado = serializers.CharField()
    especialidad = serializers.CharField()
    titulo = serializers.CharField()

class ProfesorReadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='usuario.username', read_only=True)
    email = serializers.EmailField(source='usuario.email', read_only=True)
    first_name = serializers.CharField(source='usuario.first_name', read_only=True)
    last_name = serializers.CharField(source='usuario.last_name', read_only=True)
    rol = serializers.CharField(source='usuario.rol', read_only=True)
    ci = serializers.CharField(source='usuario.ci', read_only=True)
    telefono = serializers.CharField(source='usuario.telefono', read_only=True)
    genero = serializers.CharField(source='usuario.genero', read_only=True)
    estado = serializers.CharField(source='usuario.estado', read_only=True)

    class Meta:
        model = Profesor
        fields = [
            'id', 'especialidad', 'titulo',
            'username', 'email', 'first_name', 'last_name', 'rol',
            'ci', 'telefono', 'genero', 'estado'
        ]
