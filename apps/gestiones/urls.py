from rest_framework.routers import DefaultRouter
from apps.gestiones.views.gestion_viewset import GestionViewSet

router = DefaultRouter()
router.register(r'gestiones', GestionViewSet, basename='gestion')

urlpatterns = router.urls