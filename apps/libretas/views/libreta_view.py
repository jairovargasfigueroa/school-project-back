from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.libretas.services.libreta_service import generar_libreta
from apps.usuarios.models import Alumno
from apps.gestiones.models import Gestion
from apps.usuarios.permissions import IsDocente

class LibretaAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDocente]
    def get(self, request, alumno_id, gestion_id):
        try:
            alumno = Alumno.objects.get(id=alumno_id)
            gestion = Gestion.objects.get(id=gestion_id)
            data = generar_libreta(alumno, gestion)
            return Response(data, status=status.HTTP_200_OK)
        except Alumno.DoesNotExist:
            return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Gestion.DoesNotExist:
            return Response({"error": "Gestión no encontrada"}, status=status.HTTP_404_NOT_FOUND)
