from django.shortcuts import render
from rest_framework import viewsets
from apps.curso.models.curso import Curso
from apps.curso.serializers.serializers import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
