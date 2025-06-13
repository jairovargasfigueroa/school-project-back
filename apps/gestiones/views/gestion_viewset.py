# views/gestion_viewset.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.gestiones.models import Gestion
from apps.gestiones.serializers.gestiones_serializers import GestionSerializer
from django.core.exceptions import ObjectDoesNotExist
from apps.gestiones.services.gestiones_services import GestionService
from apps.usuarios.permissions import IsDirector


class GestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsDirector]
    serializer_class = GestionSerializer

    def get_queryset(self):
        queryset = Gestion.objects.all()
        anio = self.request.query_params.get("anio")

        if anio:
            queryset = queryset.filter(anio=anio)

        return queryset

    def retrieve(self, request, pk=None):
        try:
            gestion = GestionService.obtener_gestion_por_id(pk)
            serializer = GestionSerializer(gestion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Gestión no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = GestionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                gestion = GestionService.crear_gestion(serializer.validated_data)
                return Response(GestionSerializer(gestion).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"Error al crear la gestión: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = GestionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                gestion_actualizada = GestionService.actualizar_gestion(pk, serializer.validated_data)
                return Response(GestionSerializer(gestion_actualizada).data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"error": "Gestión no encontrada."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": f"Error al actualizar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            GestionService.eliminar_gestion(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Gestión no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Error al eliminar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
