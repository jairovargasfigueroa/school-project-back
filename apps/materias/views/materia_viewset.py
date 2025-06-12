from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.materias.models import Materia
from apps.materias.serializers.materia_serializers import MateriaSerializer
from apps.materias.services.materia_service import MateriaService
from django.core.exceptions import ObjectDoesNotExist
from apps.materias.models import Materia

from django_filters import rest_framework as filters

class MateriasFilter(filters.FilterSet):
    class Meta:
        model = Materia
        fields = {
            'curso_id': ['exact'],
            'docente_id': ['exact'],
            'gestion_id': ['exact'],
        }

class MateriaViewSet(ModelViewSet):
    serializer_class = MateriaSerializer

    def get_queryset(self):
        queryset = Materia.objects.all()
        nombre = self.request.query_params.get("nombre")
        curso_id = self.request.query_params.get("curso_id")

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)

        return queryset

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
