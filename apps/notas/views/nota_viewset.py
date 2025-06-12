from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.notas.models.nota_evaluacion import NotaEvaluacion
from apps.notas.serializers.nota_serializers import NotaEvaluacionSerializer
from apps.notas.services.nota_service import NotaEvaluacionService
from django.core.exceptions import ObjectDoesNotExist

from django_filters import rest_framework as filters

class NotaFilter(filters.FilterSet):
    class Meta:
        model = NotaEvaluacion
        fields = {
            'alumno_id': ['exact'],
            'evaluacion_id': ['exact'],
            'evaluacion__tipo': ['exact', 'icontains'],
            'evaluacion__nombre': ['icontains'],
        }

class NotaEvaluacionViewSet(ViewSet):

    def list(self, request):
        notas = NotaEvaluacionService.listar_notas_evaluacion()

        filtered_queryset = NotaFilter(request.GET, queryset=notas).qs

        serializer = NotaEvaluacionSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            nota = NotaEvaluacionService.obtener_nota_por_id(pk)
            serializer = NotaEvaluacionSerializer(nota)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Nota no encontrada"}, status=404)

    # def create(self, request):
    #     serializer = NotaEvaluacionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         nota = NotaEvaluacionService.crear_nota(serializer.validated_data)
    #         return Response(NotaEvaluacionSerializer(nota).data, status=201)
    #     return Response({"error": serializer.errors}, status=400)
    
    def create(self, request):
        print("📦 Data recibida en POST:", request.data)  # Debug
        serializer = NotaEvaluacionSerializer(data=request.data)
        if serializer.is_valid():
            print("✅ Data validada:", serializer.validated_data)  # Debug
            nota = NotaEvaluacionService.crear_nota(serializer.validated_data)
            return Response(NotaEvaluacionSerializer(nota).data, status=201)
        return Response({"error": serializer.errors}, status=400)


    def update(self, request, pk=None):
        serializer = NotaEvaluacionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                nota = NotaEvaluacionService.actualizar_nota(pk, serializer.validated_data)
                return Response(NotaEvaluacionSerializer(nota).data)
            except ObjectDoesNotExist:
                return Response({"error": "Nota no encontrada"}, status=404)
        return Response({"error": serializer.errors}, status=400)

    def destroy(self, request, pk=None):
        try:
            NotaEvaluacionService.eliminar_nota(pk)
            return Response(status=204)
        except ObjectDoesNotExist:
            return Response({"error": "Nota no encontrada"}, status=404)
