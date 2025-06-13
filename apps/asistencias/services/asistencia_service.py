from apps.asistencias.models import Asistencia
from django.db import transaction
from django.shortcuts import get_object_or_404

from apps.materias.models import Materia
from apps.usuarios.models import Alumno

class AsistenciaService:

    @staticmethod
    def listar_asistencias():
        return Asistencia.objects.select_related('alumno__usuario', 'materia', 'gestion').all()

    @staticmethod
    def obtener_asistencia_por_id(asistencia_id):
        return get_object_or_404(Asistencia, id=asistencia_id)

    @staticmethod
    @transaction.atomic
    def crear_asistencia(data):
        return Asistencia.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def actualizar_asistencia(asistencia_id, data):
        asistencia = AsistenciaService.obtener_asistencia_por_id(asistencia_id)
        for attr, value in data.items():
            setattr(asistencia, attr, value)
        asistencia.save()
        return asistencia

    @staticmethod
    def eliminar_asistencia(asistencia_id):
        asistencia = AsistenciaService.obtener_asistencia_por_id(asistencia_id)
        asistencia.delete()
        
    
    @staticmethod
    def generar_asistencias_masivas(materia_id, gestion_id, fecha):
    # Obtener curso desde la materia (asumiendo materia.curso existe)
        materia = Materia.objects.select_related('curso').get(id=materia_id)
        curso = materia.curso

        alumnos = Alumno.objects.filter(curso=curso).distinct()
        asistencias = []

        for alumno in alumnos:
            obj, created = Asistencia.objects.get_or_create(
                alumno=alumno,
                curso=curso,
                materia_id=materia_id,
                gestion_id=gestion_id,
                fecha=fecha,
                defaults={'presente': False}
            )
            asistencias.append(obj)
        return asistencias
