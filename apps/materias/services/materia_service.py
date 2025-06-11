from apps.cursos.models import Curso
from apps.gestiones.models import Gestion, gestion
from apps.materias.models import Materia
from django.shortcuts import get_object_or_404
from django.db import transaction

from apps.usuarios.models import Profesor

class MateriaService:

    @staticmethod
    def listar_materias():
        return Materia.objects.select_related('curso', 'docente').all()

    @staticmethod
    def obtener_materia_por_id(materia_id):
        return get_object_or_404(Materia, id=materia_id)
    
    @staticmethod
    @transaction.atomic
    def crear_materia(data):
        curso = Curso.objects.get(id=data.pop('curso_id'))
        docente = Profesor.objects.get(id=data.pop('docente_id'))
        gestion = Gestion.objects.get(id=data.pop('gestion_id'))

        return Materia.objects.create(
            curso=curso,
            docente=docente,
            gestion=gestion,
            **data
        )

    @staticmethod
    @transaction.atomic
    def actualizar_materia(materia_id, data):
        materia = MateriaService.obtener_materia_por_id(materia_id)
        for attr, value in data.items():
            setattr(materia, attr, value)
        materia.save()
        return materia

    @staticmethod
    def eliminar_materia(materia_id):
        materia = MateriaService.obtener_materia_por_id(materia_id)
        materia.delete()
