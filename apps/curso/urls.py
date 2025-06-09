from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets.views import CursoViewSet

router = DefaultRouter()
router.register(r'curso', CursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]