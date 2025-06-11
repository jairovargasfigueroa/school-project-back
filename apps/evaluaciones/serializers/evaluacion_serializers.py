from rest_framework import serializers
from apps.evaluaciones.models import Evaluacion

class EvaluacionSerializer(serializers.ModelSerializer):
    materia_nombre = serializers.CharField(source='materia.nombre', read_only=True)
    gestion_anio = serializers.IntegerField(source='gestion.anio', read_only=True)

    # Campos de entrada (necesarios para el POST)
    materia_id = serializers.IntegerField(write_only=True)
    gestion_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Evaluacion
        fields = [
            'id',
            'nombre',
            'tipo',
            'dimension',
            'porcentaje',
            'trimestre',
            'materia_id',        # <- necesario para recibir por ID
            'gestion_id',        # <- necesario para recibir por ID
            'materia_nombre',    # <- para mostrar en el frontend
            'gestion_anio'       # <- para mostrar en el frontend
        ]
        read_only_fields = ['id', 'materia_nombre', 'gestion_anio']
