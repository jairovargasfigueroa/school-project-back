# views/profesor_viewset.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.usuarios.models import Profesor
from apps.usuarios.services.profesor_service import ProfesorService
from apps.usuarios.serializers.profesor_serializers import ProfesorWriteSerializer, ProfesorReadSerializer

class ProfesorViewSet(ModelViewSet):

    def list(self, request):
        profesores = ProfesorService.listar_profesores()
        serializer = ProfesorReadSerializer(profesores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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