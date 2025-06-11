from rest_framework.routers import DefaultRouter
from apps.materias.views.materia_viewset import MateriaViewSet

router = DefaultRouter()
router.register(r'materias', MateriaViewSet, basename='materia')

urlpatterns = router.urls
