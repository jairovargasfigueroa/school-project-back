from django.urls import path
from apps.libretas.views.libreta_view import LibretaAPIView
from apps.libretas.views.libreta_pdf_view import LibretaPDFView

urlpatterns = [
    path('<int:alumno_id>/<int:gestion_id>/', LibretaAPIView.as_view(), name='generar-libreta'),
    path('<int:alumno_id>/<int:gestion_id>/pdf/', LibretaPDFView.as_view(), name='libreta-pdf'),
]

