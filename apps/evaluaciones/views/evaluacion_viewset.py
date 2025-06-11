from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.evaluaciones.serializers.evaluacion_serializers import EvaluacionSerializer
from apps.evaluaciones.services.evaluacion_service import EvaluacionService
from django.core.exceptions import ObjectDoesNotExist

class EvaluacionViewSet(ViewSet):

    def list(self, request):
        evaluaciones = EvaluacionService.listar_evaluaciones()
        serializer = EvaluacionSerializer(evaluaciones, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            evaluacion = EvaluacionService.obtener_evaluacion_por_id(pk)
            serializer = EvaluacionSerializer(evaluacion)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Evaluación no encontrada"}, status=404)

    def create(self, request):
        serializer = EvaluacionSerializer(data=request.data)
        if serializer.is_valid():
            print("Paso al services")
            evaluacion = EvaluacionService.crear_evaluacion(serializer.validated_data)
            return Response(EvaluacionSerializer(evaluacion).data, status=201)
        return Response({"error": serializer.errors}, status=400)



    def update(self, request, pk=None):
        serializer = EvaluacionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                evaluacion = EvaluacionService.actualizar_evaluacion(pk, serializer.validated_data)
                return Response(EvaluacionSerializer(evaluacion).data)
            except ObjectDoesNotExist:
                return Response({"error": "Evaluación no encontrada"}, status=404)
        return Response({"error": serializer.errors}, status=400)

    def destroy(self, request, pk=None):
        try:
            EvaluacionService.eliminar_evaluacion(pk)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Evaluación no encontrada"}, status=404)
