from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.usuarios.models import Alumno
from apps.usuarios.serializers.alumno_serializers import AlumnoReadSerializer, AlumnoWriteSerializer
from apps.usuarios.services.alumno_service import AlumnoService
from rest_framework import status



class AlumnoViewSet(ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD sobre alumnos.
    """

    def list(self, request):
        alumnos = AlumnoService.listar_alumnos()
        serializer = AlumnoReadSerializer(alumnos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
#     def create(self, request, *args, **kwargs):
#         try:
#             #LLAMO AL SERIALIZADOR PARA VALIDAR LOS DATOS DEL ALUMNO
#             serializer = self.get_serializer(data = request.data)
#             serializer.is_valid(raise_exception=True)
#             alumno = crear_Alumno(serializer.validated_data)
#             return Response({
#                 "message": "Alumno creado exitosamente",
#                 "data": self.get_serializer(alumno).data
#             }, status=status.HTTP_201_CREATED)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
#         except Exception as e:
#             return Response({"error": "An unexpected error occurred."}, status=500)
            
#     def update(self, request, *args, **kwargs):
#         try:
#             # Obtengo el objeto Alumno a actualizar
#             alumno = self.get_object()
#             serializer = self.get_serializer(alumno, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             alumno = serializer.save()
#             return Response({
#                 "message": "Alumno actualizado exitosamente",
#                 "data": self.get_serializer(alumno).data
#             }, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
#         except Exception as e:
#             return Response({"error": "An unexpected error occurred."}, status=500)
    
#     def destroy(self, request, *args, **kwargs):
#         try:
#             # Obtengo el objeto Alumno a eliminar
#             alumno = self.get_object()
#             alumno.delete()
#             return Response({"message": "Alumno eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
#         except Exception as e:
#             return Response({"error": "An unexpected error occurred."}, status=500)
        
#     def retrieve(self, request, *args, **kwargs):
#         try:
#             # Obtengo el objeto Alumno por ID
#             alumno = self.get_object()
#             return Response(self.get_serializer(alumno).data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
#         except Exception as e:
#             return Response({"error": "An unexpected error occurred."}, status=500)                
    
#     def list(self, request, *args, **kwargs):
#         try:
#             # Obtengo todos los objetos Alumno
#             alumnos = self.get_queryset()
#             serializer = self.get_serializer(alumnos, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
#         except Exception as e:
#             return Response({"error": "An unexpected error occurred."}, status=500)
    
   
   