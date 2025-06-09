from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.usuarios.views.alumno_viewset import AlumnoViewSet




router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumnos')

urlpatterns = router.urls + [
    # path('login/', LoginView.as_view(), name='login'),
    # path('perfil/', AlumnoPerfilView.as_view(), name='perfil-alumno'),
]