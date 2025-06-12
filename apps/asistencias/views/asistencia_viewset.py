from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.asistencias.models.asistencia import Asistencia
from apps.asistencias.serializers.asistencia_serilaizers import AsistenciaSerializer
from apps.asistencias.services.asistencia_service import AsistenciaService
from django.core.exceptions import ObjectDoesNotExist

from django_filters import rest_framework as filters


class AsistenciaFilter(filters.FilterSet):
    class Meta:
        model = Asistencia
        fields = ['alumno', 'materia', 'gestion', 'fecha', 'alumno__usuario__first_name']


class AsistenciaViewSet(ViewSet):

    def list(self, request):
        asistencias = AsistenciaService.listar_asistencias()

        filtered_queryset = AsistenciaFilter(request.GET, queryset=asistencias).qs

        serializer = AsistenciaSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            asistencia = AsistenciaService.obtener_asistencia_por_id(pk)
            serializer = AsistenciaSerializer(asistencia)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Asistencia no encontrada"}, status=404)

    def create(self, request):
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            asistencia = AsistenciaService.crear_asistencia(serializer.validated_data)
            return Response(AsistenciaSerializer(asistencia).data, status=201)
        return Response({"error": serializer.errors}, status=400)

    def update(self, request, pk=None):
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                asistencia = AsistenciaService.actualizar_asistencia(pk, serializer.validated_data)
                return Response(AsistenciaSerializer(asistencia).data)
            except ObjectDoesNotExist:
                return Response({"error": "Asistencia no encontrada"}, status=404)
        return Response({"error": serializer.errors}, status=400)

    def destroy(self, request, pk=None):
        try:
            AsistenciaService.eliminar_asistencia(pk)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Asistencia no encontrada"}, status=404)
