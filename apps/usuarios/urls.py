from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.usuarios.views.alumno_viewset import AlumnoViewSet
from apps.usuarios.views.director_viewset import DirectorViewSet
from apps.usuarios.views.profesor_viewset import ProfesorViewSet




router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')
router.register(r'profesores', ProfesorViewSet, basename='profesores')
router.register(r'directores', DirectorViewSet, basename='directores')

urlpatterns = router.urls + [
    # path('login/', LoginView.as_view(), name='login'),
    # path('perfil/', AlumnoPerfilView.as_view(), name='perfil-alumno'),
]