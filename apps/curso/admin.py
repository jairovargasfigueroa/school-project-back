from django.contrib import admin
from apps.curso.models.curso import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'turno', 'gestion')
    list_filter = ('nivel', 'turno', 'gestion')
    search_fields = ('nombre',)
