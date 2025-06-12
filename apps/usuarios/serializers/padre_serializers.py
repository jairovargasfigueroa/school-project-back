from rest_framework import serializers
from apps.usuarios.models import Padre
from apps.usuarios.models import Alumno

class PadreReadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='usuario.username')
    email = serializers.EmailField(source='usuario.email')
    first_name = serializers.CharField(source='usuario.first_name')
    last_name = serializers.CharField(source='usuario.last_name')
    rol = serializers.CharField(source='usuario.rol')
    ci = serializers.CharField(source='usuario.ci')
    telefono = serializers.CharField(source='usuario.telefono')
    genero = serializers.CharField(source='usuario.genero')
    estado = serializers.CharField(source='usuario.estado')

    class Meta:
        model = Padre
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'rol',
            'ci', 'telefono', 'genero', 'estado', 'ocupacion', 'alumnos'
        ]

class PadreWriteSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    rol = serializers.CharField()
    ci = serializers.CharField()
    telefono = serializers.CharField()
    genero = serializers.CharField()
    estado = serializers.CharField()
    ocupacion = serializers.CharField()
