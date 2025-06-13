from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from apps.usuarios.views.alumno_viewset import AlumnoViewSet
from apps.usuarios.views.director_viewset import DirectorViewSet
from apps.usuarios.views.login_view import CustomTokenObtainPairView
from apps.usuarios.views.padre_viewset import PadreViewSet
from apps.usuarios.views.profesor_viewset import ProfesorViewSet




router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'profesores', ProfesorViewSet, basename='profesores')
router.register(r'directores', DirectorViewSet, basename='directores')
router.register(r'padres',PadreViewSet, basename='padres')

urlpatterns = router.urls + [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ Ruta extra
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]