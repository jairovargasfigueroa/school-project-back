from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.notas.models import NotaEvaluacion
from apps.notas.serializers.nota_serializers import NotaEvaluacionSerializer
from apps.notas.services.nota_service import NotaEvaluacionService
from django.core.exceptions import ObjectDoesNotExist

from apps.usuarios.permissions import IsAlumno, IsDocente

class NotaEvaluacionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsDocente,IsAlumno]
    serializer_class = NotaEvaluacionSerializer

    def get_queryset(self):
        queryset = NotaEvaluacion.objects.select_related( "evaluacion", "alumno")
        alumno_id = self.request.query_params.get("alumno_id")
        materia_id = self.request.query_params.get("materia_id")
        gestion_id = self.request.query_params.get("gestion_id")

        # if alumno_id:
        #     queryset = queryset.filter(alumno_id=alumno_id)
        # if materia_id:
        #     queryset = queryset.filter(materia_id=materia_id)
        if gestion_id:
            queryset = queryset.filter(evaluacion__gestion_id=gestion_id)

        return queryset

    def retrieve(self, request, pk=None):
        try:
            nota = NotaEvaluacionService.obtener_nota_por_id(pk)
            serializer = NotaEvaluacionSerializer(nota)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Nota no encontrada"}, status=404)
    
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
