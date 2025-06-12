from rest_framework import serializers
from apps.notas.models import NotaEvaluacion

class NotaEvaluacionSerializer(serializers.ModelSerializer):
    alumno_nombre = serializers.CharField(source='alumno.usuario.get_full_name', read_only=True)
    evaluacion_nombre = serializers.CharField(source='evaluacion.nombre', read_only=True)
    tipo_evaluacion = serializers.CharField(source='evaluacion.tipo', read_only=True)

    alumno_id = serializers.IntegerField()
    evaluacion_id = serializers.IntegerField()
    class Meta:
        model = NotaEvaluacion
        fields = ['id', 'nota','alumno_id', 'alumno_nombre', 'evaluacion_id','evaluacion_nombre', 'tipo_evaluacion']
