from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data['user_id'] = user.id
        data['rol'] = user.rol
        data['username'] = user.username
        data['nombre_completo'] = user.get_full_name()

        if user.rol == 'alumno' and hasattr(user, 'alumno'):
            alumno = user.alumno
            data['alumno_id'] = alumno.id
            data['curso_id'] = alumno.curso_id
            data['fecha_nacimiento'] = str(alumno.fecha_nacimiento)

        elif user.rol == 'docente' and hasattr(user, 'profesor'):
            profe = user.profesor
            data['profesor_id'] = profe.id
            # puedes agregar más datos aquí

        elif user.rol == 'director' and hasattr(user, 'director'):
            data['director_id'] = user.director.id

        elif user.rol == 'padre' and hasattr(user, 'padre'):
            data['padre_id'] = user.padre.id

        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
