from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.cursos.serializers.curso_serializers import CursoSerializer
from django.core.exceptions import ObjectDoesNotExist
from apps.cursos.services.curso_service import CursoService


class CursoViewSet(ViewSet):
    """
    ViewSet para gestionar CRUD de cursos.
    """

    def list(self, request):
        cursos = CursoService.listar_cursos()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            curso = CursoService.obtener_curso_por_id(pk)
            serializer = CursoSerializer(curso)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Curso no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                curso = CursoService.crear_curso(serializer.validated_data)
                return Response(CursoSerializer(curso).data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": f"Error al crear el curso: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                curso_actualizado = CursoService.actualizar_curso(pk, serializer.validated_data)
                return Response(CursoSerializer(curso_actualizado).data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"error": "Curso no encontrado."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": f"Error al actualizar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            CursoService.eliminar_curso(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Curso no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Error al eliminar: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
