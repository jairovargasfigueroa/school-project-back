from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'turno', 'gestion')
    list_filter = ('nivel', 'turno', 'gestion')
    search_fields = ('nombre',)
