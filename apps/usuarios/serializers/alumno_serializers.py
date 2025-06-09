
# from rest_framework import serializers
# from apps.usuarios.models import Alumno




# #Clase para definir las validaciones y la estructura de los datos del modelo Alumno
# class AlumnoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Alumno
#         fields = '__all__'  # Serialize all fields of the Alumno model

#     def validate(self, data):
#         """
#         Validates the data for the Alumno model.
#         :param data: Dictionary containing the data to validate.
#         :return: Validated data.
#         """
#         # Example validation: Ensure 'nombre' is not empty
#         if len(data.get('telefono')) < 5:
#             raise serializers.ValidationError("El campo 'telefono' debe tener al menos 8 caracteres.")
#             # raise serializers.ValidationError("El campo 'nombre' es obligatorio.")
        
#         # Add more validations as needed
#         return data

import re
from rest_framework import serializers
from apps.usuarios.models import Alumno, Usuario

class AlumnoWriteSerializer(serializers.Serializer):
    """Serializer para creación/actualización de alumnos (POST, PUT)"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,required=False)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    rol = serializers.ChoiceField(choices=Usuario.Rol.choices)
    ci = serializers.CharField()
    telefono = serializers.CharField()
    genero = serializers.CharField()
    estado = serializers.CharField()

    codigo = serializers.CharField()
    fecha_nacimiento = serializers.DateField()
    direccion = serializers.CharField()


class AlumnoReadSerializer(serializers.ModelSerializer):
    """Serializer solo para lectura (GET)"""
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
        model = Alumno
        fields = [
            'id',
            'codigo',
            'fecha_nacimiento',
            'direccion',
            'username',
            'email',
            'first_name',
            'last_name',
            'rol',
            'ci',
            'telefono',
            'genero',
            'estado'
        ]