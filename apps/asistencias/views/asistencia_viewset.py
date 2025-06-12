from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.asistencias.models import Asistencia
from apps.asistencias.serializers.asistencia_serilaizers import AsistenciaSerializer
from apps.asistencias.services.asistencia_service import AsistenciaService
from django.core.exceptions import ObjectDoesNotExist

class AsistenciaViewSet(ModelViewSet):
    serializer_class = AsistenciaSerializer

    def get_queryset(self):
        queryset = Asistencia.objects.select_related("alumno", "materia")
        # alumno_id = self.request.query_params.get("alumno_id")
        # curso_id = self.request.query_params.get("curso_id")
        # fecha = self.request.query_params.get("fecha")

        # if alumno_id:
        #     queryset = queryset.filter(alumno_id=alumno_id)
        # if curso_id:
        #     queryset = queryset.filter(curso_id=curso_id)
        # if fecha:
        #     queryset = queryset.filter(fecha=fecha)

        return queryset

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
