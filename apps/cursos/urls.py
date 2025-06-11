from rest_framework.routers import DefaultRouter
from apps.cursos.views.curso_viewset import CursoViewSet


router = DefaultRouter()
router.register(r'cursos', CursoViewSet, basename='cursos')

urlpatterns = router.urls