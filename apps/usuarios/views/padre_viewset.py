from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.usuarios.models import Padre

from apps.usuarios.serializers.padre_serializers import PadreReadSerializer, PadreWriteSerializer
from apps.usuarios.services.padre_service import PadreService

class PadreViewSet(ModelViewSet):
    
    def get_queryset(self):
        queryset = Padre.objects.select_related("usuario")

        # Filtrar por CI del usuario (padre)
        ci = self.request.query_params.get("ci")
        if ci:
            queryset = queryset.filter(usuario__ci__icontains=ci)

        # Filtrar por ocupación
        ocupacion = self.request.query_params.get("ocupacion")
        if ocupacion:
            queryset = queryset.filter(ocupacion__icontains=ocupacion)

        return queryset


    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PadreReadSerializer
        return PadreWriteSerializer

    def retrieve(self, request, pk=None):
        padre = PadreService.obtener_padre_por_id(pk)
        if padre:
            serializer = PadreReadSerializer(padre)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Padre no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = PadreWriteSerializer(data=request.data)
        if serializer.is_valid():
            padre = PadreService.crear_padre(serializer.validated_data)
            read_serializer = PadreReadSerializer(padre)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = PadreWriteSerializer(data=request.data)
        if serializer.is_valid():
            padre_actualizado = PadreService.actualizar_padre(pk, serializer.validated_data)
            if padre_actualizado:
                read_serializer = PadreReadSerializer(padre_actualizado)
                return Response(read_serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Padre no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if PadreService.eliminar_padre(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Padre no encontrado"}, status=status.HTTP_404_NOT_FOUND)
