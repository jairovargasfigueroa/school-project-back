from rest_framework import serializers
from apps.materias.models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    curso_id = serializers.IntegerField()
    docente_id = serializers.IntegerField()
    gestion_id = serializers.IntegerField()

    curso_nombre = serializers.CharField(source='curso.nombre', read_only=True)
    docente_nombre = serializers.CharField(source='docente.usuario.get_full_name', read_only=True)
    gestion_anio = serializers.IntegerField(source='gestion.anio', read_only=True)

    class Meta:
        model = Materia
        fields = [
            'id',
            'nombre',
            'descripcion',
            'curso_id',
            'docente_id',
            'gestion_id',
            'curso_nombre',
            'docente_nombre',
            'gestion_anio'
        ]
        read_only_fields = ['id', 'curso_nombre', 'docente_nombre', 'gestion_anio']