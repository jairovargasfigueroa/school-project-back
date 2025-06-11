from apps.cursos.models import Curso
from django.db import transaction
from django.shortcuts import get_object_or_404

class CursoService:

    @staticmethod
    def listar_cursos():
        return Curso.objects.all()

    @staticmethod
    def obtener_curso_por_id(curso_id):
        return get_object_or_404(Curso, id=curso_id)

    @staticmethod
    @transaction.atomic
    def crear_curso(data):
        return Curso.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def actualizar_curso(curso_id, data):
        curso = CursoService.obtener_curso_por_id(curso_id)
        for attr, value in data.items():
            setattr(curso, attr, value)
        curso.save()
        return curso

    @staticmethod
    def eliminar_curso(curso_id):
        curso = CursoService.obtener_curso_por_id(curso_id)
        curso.delete()