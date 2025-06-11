from apps.evaluaciones.models import Evaluacion
from django.shortcuts import get_object_or_404
from django.db import transaction

from apps.gestiones.models import Gestion
from apps.materias.models import Materia

class EvaluacionService:

    @staticmethod
    def listar_evaluaciones():
        return Evaluacion.objects.select_related('materia', 'gestion').all()

    @staticmethod
    def obtener_evaluacion_por_id(evaluacion_id):
        return get_object_or_404(Evaluacion, id=evaluacion_id)

    @staticmethod
    @transaction.atomic
    def crear_evaluacion(data):
        print("DATA ENTRANTE:", data)  # 🐞
        materia = Materia.objects.get(id=data.pop('materia_id'))
        gestion = Gestion.objects.get(id=data.pop('gestion_id'))

        return Evaluacion.objects.create(
            materia=materia,
            gestion=gestion,
            **data
        )
        

    @staticmethod
    @transaction.atomic
    def actualizar_evaluacion(evaluacion_id, data):
        evaluacion = EvaluacionService.obtener_evaluacion_por_id(evaluacion_id)
        for attr, value in data.items():
            setattr(evaluacion, attr, value)
        evaluacion.save()
        return evaluacion

    @staticmethod
    def eliminar_evaluacion(evaluacion_id):
        evaluacion = EvaluacionService.obtener_evaluacion_por_id(evaluacion_id)
        evaluacion.delete()
