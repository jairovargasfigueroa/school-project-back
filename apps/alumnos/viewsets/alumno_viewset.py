import re
from rest_framework import viewsets
from rest_framework.response import Response

from apps.alumnos.models import Alumno, alumno
from apps.alumnos.serializers.alumno_serializers import AlumnoSerializer
from apps.alumnos.services.alumno_service import crear_Alumno
from rest_framework import status



class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            #LLAMO AL SERIALIZADOR PARA VALIDAR LOS DATOS DEL ALUMNO
            serializer = self.get_serializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            alumno = crear_Alumno(serializer.validated_data)
            return Response({
                "message": "Alumno creado exitosamente",
                "data": self.get_serializer(alumno).data
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=500)
            
    def update(self, request, *args, **kwargs):
        try:
            # Obtengo el objeto Alumno a actualizar
            alumno = self.get_object()
            serializer = self.get_serializer(alumno, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            alumno = serializer.save()
            return Response({
                "message": "Alumno actualizado exitosamente",
                "data": self.get_serializer(alumno).data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=500)
    
    def destroy(self, request, *args, **kwargs):
        try:
            # Obtengo el objeto Alumno a eliminar
            alumno = self.get_object()
            alumno.delete()
            return Response({"message": "Alumno eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=500)
        
    def retrieve(self, request, *args, **kwargs):
        try:
            # Obtengo el objeto Alumno por ID
            alumno = self.get_object()
            return Response(self.get_serializer(alumno).data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=500)                
    
    def list(self, request, *args, **kwargs):
        try:
            # Obtengo todos los objetos Alumno
            alumnos = self.get_queryset()
            serializer = self.get_serializer(alumnos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=500)
    
   