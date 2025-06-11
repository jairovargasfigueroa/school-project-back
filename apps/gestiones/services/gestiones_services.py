from django.shortcuts import get_object_or_404
from django.db import transaction
from apps.gestiones.models import Gestion

class GestionService:

    @staticmethod
    def listar_gestiones():
        return Gestion.objects.all()

    @staticmethod
    def obtener_gestion_por_id(gestion_id):
        return get_object_or_404(Gestion, id=gestion_id)

    @staticmethod
    @transaction.atomic
    def crear_gestion(data):
        return Gestion.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def actualizar_gestion(gestion_id, data):
        gestion = GestionService.obtener_gestion_por_id(gestion_id)
        for attr, value in data.items():
            setattr(gestion, attr, value)
        gestion.save()
        return gestion

    @staticmethod
    def eliminar_gestion(gestion_id):
        gestion = GestionService.obtener_gestion_por_id(gestion_id)
        gestion.delete()

