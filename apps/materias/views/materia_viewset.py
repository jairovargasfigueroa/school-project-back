from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.materias.serializers.materia_serializers import MateriaSerializer
from apps.materias.services.materia_service import MateriaService
from django.core.exceptions import ObjectDoesNotExist

class MateriaViewSet(ViewSet):
    """
    ViewSet para gestionar materias.
    """

    def list(self, request):
        materias = MateriaService.listar_materias()
        serializer = MateriaSerializer(materias, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            materia = MateriaService.obtener_materia_por_id(pk)
            serializer = MateriaSerializer(materia)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Materia no encontrada"}, status=404)

    def create(self, request):
        serializer = MateriaSerializer(data=request.data)
        if serializer.is_valid():
            materia = MateriaService.crear_materia(serializer.validated_data)
            return Response(MateriaSerializer(materia).data, status=201)
        return Response({"error": serializer.errors}, status=400)

    def update(self, request, pk=None):
        serializer = MateriaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                materia = MateriaService.actualizar_materia(pk, serializer.validated_data)
                return Response(MateriaSerializer(materia).data)
            except ObjectDoesNotExist:
                return Response({"error": "Materia no encontrada"}, status=404)
        return Response({"error": serializer.errors}, status=400)

    def destroy(self, request, pk=None):
        try:
            MateriaService.eliminar_materia(pk)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Materia no encontrada"}, status=404)
