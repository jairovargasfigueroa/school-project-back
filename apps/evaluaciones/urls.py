from rest_framework.routers import DefaultRouter
from apps.evaluaciones.views.evaluacion_viewset import EvaluacionViewSet

router = DefaultRouter()
router.register(r'evaluaciones', EvaluacionViewSet, basename='evaluacion')

urlpatterns = router.urls
