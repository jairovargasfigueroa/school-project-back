from apps.notas.models import NotaEvaluacion
from django.shortcuts import get_object_or_404
from django.db import transaction

class NotaEvaluacionService:

    @staticmethod
    def listar_notas_evaluacion():
        return NotaEvaluacion.objects.select_related('evaluacion', 'alumno__usuario').all()

    @staticmethod
    def obtener_nota_por_id(nota_id):
        return get_object_or_404(NotaEvaluacion, id=nota_id)

    @staticmethod
    @transaction.atomic
    def crear_nota(data):
        alumno_id = data.get('alumno_id')
        evaluacion_id = data.get('evaluacion_id')
        nota_valor = data.get('nota')

        if not alumno_id or not evaluacion_id or nota_valor is None:
            raise ValueError("Datos insuficientes para crear la nota")

        return NotaEvaluacion.objects.create(
            alumno_id=alumno_id,
            evaluacion_id=evaluacion_id,
            nota=nota_valor
        )


    @staticmethod
    @transaction.atomic
    def actualizar_nota(nota_id, data):
        nota = NotaEvaluacionService.obtener_nota_por_id(nota_id)
        for attr, value in data.items():
            setattr(nota, attr, value)
        nota.save()
        return nota

    @staticmethod
    def eliminar_nota(nota_id):
        nota = NotaEvaluacionService.obtener_nota_por_id(nota_id)
        nota.delete()
