from rest_framework import serializers

from apps.curso.models.curso import Curso, Materia

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'nivel', 'turno', 'gestion']

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ['id', 'nombre', 'descripcion', 'curso_id']