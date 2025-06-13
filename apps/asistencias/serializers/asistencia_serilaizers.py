from rest_framework import serializers
from apps.asistencias.models import Asistencia

class AsistenciaSerializer(serializers.ModelSerializer):
    alumno_nombre = serializers.CharField(source='alumno.usuario.get_full_name', read_only=True)
    materia_nombre = serializers.CharField(source='materia.nombre', read_only=True)
    gestion_anio = serializers.IntegerField(source='gestion.anio', read_only=True)
    curso_nombre = serializers.CharField(source='curso.nombre', read_only=True)    
    class Meta:
        model = Asistencia
        fields = ['id', 'alumno', 'materia','curso', 'gestion', 'fecha', 'presente','curso_nombre', 'alumno_nombre', 'materia_nombre', 'gestion_anio']
