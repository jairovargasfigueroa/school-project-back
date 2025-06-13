from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.usuarios.models import Alumno
from apps.usuarios.permissions import IsDocente
from apps.usuarios.serializers.alumno_serializers import AlumnoReadSerializer, AlumnoWriteSerializer
from apps.usuarios.services.alumno_service import AlumnoService
from rest_framework import status



class AlumnoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsDocente]
    
    def get_queryset(self):
        queryset = Alumno.objects.select_related("usuario", "curso")
        curso_id = self.request.query_params.get("curso_id")

        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)

        return queryset


    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AlumnoReadSerializer
        return AlumnoWriteSerializer


    def retrieve(self, request, pk=None):
        alumno = AlumnoService.obtener_alumno_por_id(pk)
        if alumno:
            serializer = AlumnoReadSerializer(alumno)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = AlumnoWriteSerializer(data=request.data)
        if serializer.is_valid():
            alumno = AlumnoService.crear_alumno(serializer.validated_data)
            read_serializer = AlumnoReadSerializer(alumno)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = AlumnoWriteSerializer(data=request.data)
        if serializer.is_valid():
            alumno_actualizado = AlumnoService.actualizar_alumno(pk, serializer.validated_data)
            if alumno_actualizado:
                read_serializer = AlumnoReadSerializer(alumno_actualizado)
                return Response(read_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if AlumnoService.eliminar_alumno(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
