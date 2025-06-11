from rest_framework.routers import DefaultRouter

from apps.notas.views.nota_viewset import NotaEvaluacionViewSet

router = DefaultRouter()
router.register(r'notas-evaluacion', NotaEvaluacionViewSet, basename='nota-evaluacion')

urlpatterns = router.urls
