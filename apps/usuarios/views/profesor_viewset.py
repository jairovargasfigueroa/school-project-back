# views/profesor_viewset.py
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.usuarios.models import Profesor
from apps.usuarios.permissions import IsDirector
from apps.usuarios.services.profesor_service import ProfesorService
from apps.usuarios.serializers.profesor_serializers import ProfesorWriteSerializer, ProfesorReadSerializer

class ProfesorViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated, IsDirector]
    permission_classes = [AllowAny]
    serializer_class = ProfesorReadSerializer

    def get_queryset(self):
        queryset = Profesor.objects.select_related("usuario")
        materia_id = self.request.query_params.get("materia_id")
        curso_id = self.request.query_params.get("curso_id")

        if materia_id:
            queryset = queryset.filter(materias__id=materia_id)
        if curso_id:
            queryset = queryset.filter(cursos__id=curso_id)

        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProfesorReadSerializer
        return ProfesorWriteSerializer

    def retrieve(self, request, pk=None):
        profesor = ProfesorService.obtener_profesor_por_id(pk)
        if profesor:
            serializer = ProfesorReadSerializer(profesor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        serializer = ProfesorWriteSerializer(data=request.data)
        if serializer.is_valid():
            profesor = ProfesorService.crear_profesor(serializer.validated_data)
            read_serializer = ProfesorReadSerializer(profesor)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = ProfesorWriteSerializer(data=request.data)
        if serializer.is_valid():
            profesor_actualizado = ProfesorService.actualizar_profesor(pk, serializer.validated_data)
            if profesor_actualizado:
                read_serializer = ProfesorReadSerializer(profesor_actualizado)
                return Response(read_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if ProfesorService.eliminar_profesor(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Profesor no encontrado"}, status=status.HTTP_404_NOT_FOUND)