"""
URL configuration for school_project_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.usuarios.urls')),  # <-- aquí se incluyen las rutas de alumnos
    path('api/', include('apps.cursos.urls')),  # <-- aquí se incluyen las rutas de cursos
    path('api/', include('apps.gestiones.urls')),  # <-- aquí se incluyen las rutas de gestiones
    path('api/', include('apps.materias.urls')),  # <-- aquí se incluyen las rutas de materias
    path('api/', include('apps.evaluaciones.urls')),  # <-- aquí se incluyen las rutas de evaluaciones
    path('api/', include('apps.notas.urls')),  # <-- aquí se incluyen las rutas de notas
    path('api/', include('apps.asistencias.urls')),  # <-- aquí se incluyen las rutas de asistencias
    path('api/libretas/', include('apps.libretas.urls')),  # <-- aquí se incluyen las rutas de libretas
]
