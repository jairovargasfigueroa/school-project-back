from rest_framework.routers import DefaultRouter
from apps.asistencias.views.asistencia_viewset import AsistenciaViewSet

router = DefaultRouter()
router.register(r'asistencias', AsistenciaViewSet, basename='asistencia')

urlpatterns = router.urls
