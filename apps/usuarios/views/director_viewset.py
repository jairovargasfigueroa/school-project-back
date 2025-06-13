# apps/usuarios/views/director_viewset.py
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from apps.usuarios.models import Director
from apps.usuarios.permissions import IsDirector
from apps.usuarios.services.director_service import DirectorService
from apps.usuarios.serializers.director_serializers import DirectorWriteSerializer, DirectorReadSerializer

class DirectorViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = DirectorReadSerializer

    def get_queryset(self):
        queryset = Director.objects.select_related("usuario")
        gestion_id = self.request.query_params.get("gestion_id")

        if gestion_id:
            queryset = queryset.filter(gestion_id=gestion_id)

        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DirectorReadSerializer
        return DirectorWriteSerializer


    def retrieve(self, request, pk=None):
        director = DirectorService.obtener_director_por_id(pk)
        if director:
            serializer = DirectorReadSerializer(director)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Director no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = DirectorWriteSerializer(data=request.data)
        if serializer.is_valid():
            director = DirectorService.crear_director(serializer.validated_data)
            read_serializer = DirectorReadSerializer(director)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = DirectorWriteSerializer(data=request.data)
        if serializer.is_valid():
            director_actualizado = DirectorService.actualizar_director(pk, serializer.validated_data)
            if director_actualizado:
                read_serializer = DirectorReadSerializer(director_actualizado)
                return Response(read_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Director no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if DirectorService.eliminar_director(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Director no encontrado"}, status=status.HTTP_404_NOT_FOUND)
