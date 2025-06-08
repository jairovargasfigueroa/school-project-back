from rest_framework.routers import DefaultRouter
from apps.alumnos.viewsets.alumno_viewset import AlumnoViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, basename='alumno')

urlpatterns = router.urls