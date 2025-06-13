
# import os
# import django
# import random
# from datetime import date, timedelta
# from faker import Faker

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()

# from django.contrib.auth import get_user_model
# from apps.usuarios.models import Alumno, Profesor, Director
# from apps.cursos.models import Curso
# from apps.gestiones.models import Gestion
# from apps.materias.models import Materia
# from apps.evaluaciones.models import Evaluacion
# from apps.notas.models import NotaEvaluacion
# from apps.asistencias.models import Asistencia

# User = get_user_model()
# fake = Faker()

# def crear_gestion(anio):
#     gestion, _ = Gestion.objects.get_or_create(anio=anio, defaults={'descripcion': f"Gestión {anio}", 'activa': False})
#     return gestion

# def crear_cursos():
#     niveles = ['primaria', 'secundaria']
#     turnos = ['mañana', 'tarde', 'noche']
#     cursos = []
#     for nivel in niveles:
#         for turno in turnos:
#             for grado in range(1, 7):
#                 nombre = f"{grado}° {nivel.capitalize()} - {turno.capitalize()}"
#                 curso, _ = Curso.objects.get_or_create(
#                     nombre=nombre,
#                     defaults={
#                         'descripcion': f"Curso {nombre}",
#                         'nivel': nivel,
#                         'turno': turno
#                     }
#                 )
#                 cursos.append(curso)
#     return cursos

# def crear_usuarios_y_roles(cursos):
#     profesores = []
#     alumnos = []
#     materias_nombres = ['Matemáticas', 'Lenguaje', 'Física', 'Química', 'Música', 'Psicología', 'Religión', 'Educación Física']

#     for curso in cursos:
#         # Crear 30 alumnos por curso
#         for _ in range(30):
#             nombre = fake.first_name()
#             apellido = fake.last_name()
#             username = f"{nombre.lower()}.{apellido.lower()}{random.randint(1, 999)}"
#             user = User.objects.create_user(
#                 username=username,
#                 password='test1234',
#                 first_name=nombre,
#                 last_name=apellido,
#                 rol='alumno',
#                 ci=fake.random_number(digits=7),
#                 telefono=fake.phone_number(),
#                 genero=random.choice(['M', 'F']),
#                 estado='activo'
#             )
#             Alumno.objects.create(
#                 usuario=user,
#                 codigo=f"AL{random.randint(1000,9999)}",
#                 fecha_nacimiento=fake.date_of_birth(minimum_age=10, maximum_age=18),
#                 direccion=fake.address(),
#                 curso=curso
#             )

#         for nombre_materia in materias_nombres:
#             # Crear profesor solo si no hay suficientes
#             nombre_prof = fake.first_name()
#             apellido_prof = fake.last_name()
#             username = f"{nombre_prof.lower()}.{apellido_prof.lower()}{random.randint(1, 999)}"
#             user = User.objects.create_user(
#                 username=username,
#                 password='test1234',
#                 first_name=nombre_prof,
#                 last_name=apellido_prof,
#                 rol='docente',
#                 ci=fake.random_number(digits=7),
#                 telefono=fake.phone_number(),
#                 genero=random.choice(['M', 'F']),
#                 estado='activo'
#             )
#             profesor = Profesor.objects.create(usuario=user, especialidad='General', titulo='Licenciatura')
#             profesores.append(profesor)

#             Materia.objects.create(
#                 nombre=nombre_materia,
#                 descripcion=f"Materia de {nombre_materia}",
#                 curso=curso,
#                 docente=profesor,
#                 gestion=gestion_2024
#             )

# def crear_evaluaciones_y_notas(gestion):
#     trimestres = [1, 2, 3]
#     dimensiones = ['ser', 'saber', 'hacer', 'decidir']
#     tipos = ['examen', 'tarea', 'participacion']

#     materias = Materia.objects.filter(gestion=gestion)
#     for materia in materias:
#         for trimestre in trimestres:
#             for i in range(3):  # 3 evaluaciones por trimestre
#                 evaluacion = Evaluacion.objects.create(
#                     nombre=f"Eval {i+1} - T{trimestre}",
#                     tipo=random.choice(tipos),
#                     dimension=random.choice(dimensiones),
#                     porcentaje=random.choice([20, 25, 30]),
#                     trimestre=trimestre,
#                     materia=materia,
#                     gestion=gestion
#                 )
#                 for alumno in Alumno.objects.filter(curso=materia.curso):
#                     NotaEvaluacion.objects.create(
#                         evaluacion=evaluacion,
#                         alumno=alumno,
#                         nota=round(random.uniform(30, 100), 2)
#                     )

# def crear_asistencias(gestion):
#     materias = Materia.objects.filter(gestion=gestion)
#     for materia in materias:
#         for alumno in Alumno.objects.filter(curso=materia.curso):
#             for i in range(10):  # 10 asistencias por alumno y materia
#                 fecha = date(gestion.anio, 3, 1) + timedelta(days=i)
#                 Asistencia.objects.create(
#                     alumno=alumno,
#                     materia=materia,
#                     gestion=gestion,
#                     fecha=fecha,
#                     presente=random.choice([True, True, False])
#                 )

# if __name__ == "__main__":
#     print("📌 Iniciando carga de datos para Gestión 2024...")
#     gestion_2024 = crear_gestion(2024)
#     cursos = crear_cursos()
#     crear_usuarios_y_roles(cursos)
#     crear_evaluaciones_y_notas(gestion_2024)
#     crear_asistencias(gestion_2024)
#     print("✅ Base de datos poblada correctamente con datos de ejemplo.")



import os
import django
import random
from datetime import date, timedelta
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE','school_project_back.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.usuarios.models import Alumno, Profesor, Padre
from apps.cursos.models import Curso
from apps.gestiones.models import Gestion
from apps.materias.models import Materia
from apps.evaluaciones.models import Evaluacion
from apps.notas.models import NotaEvaluacion
from apps.asistencias.models import Asistencia


User = get_user_model()
fake = Faker()

def crear_gestion(anio):
    gestion, created = Gestion.objects.get_or_create(anio=anio, defaults={
        'descripcion': f"Gestión {anio}",
        'activa': False
    })
    print(f"{'✔️ Creada' if created else 'ℹ️ Ya existía'} la gestión {anio}")
    return gestion

def crear_cursos():
    niveles = ['primaria', 'secundaria']
    turnos = ['mañana', 'tarde', 'noche']
    cursos = []
    for nivel in niveles:
        for turno in turnos:
            for grado in range(1, 7):
                nombre = f"{grado}° {nivel.capitalize()} - {turno.capitalize()}"
                curso, created = Curso.objects.get_or_create(
                    nombre=nombre,
                    defaults={
                        'descripcion': f"Curso {nombre}",
                        'nivel': nivel,
                        'turno': turno
                    }
                )
                cursos.append(curso)
                print(f"{'✔️ Creado' if created else 'ℹ️ Ya existía'} curso: {nombre}")
    return cursos

def crear_profesores():
    profesores = []
    for _ in range(20):
        nombre = fake.first_name()
        apellido = fake.last_name()
        username = f"{nombre.lower()}.{apellido.lower()}{random.randint(100, 150)}"
        # print(f"Creando profesor: {username} ({nombre} {apellido})")
        user = User.objects.create_user(
            username=username[:150],  # asegurar límite
            password='test1234',
            first_name=nombre[:30],
            last_name=apellido[:30],
            rol='docente',
            ci=str(fake.random_number(digits=10))[:20],
            telefono=fake.numerify(text="##########")[:20],
            genero=random.choice(['M', 'F', 'O']),  # correcto según tu modelo
            estado='activo'[:15]  # asegurar límite de 15 caracteres
        )
        profesor = Profesor.objects.create(usuario=user, especialidad='General', titulo='Licenciatura')
        profesores.append(profesor)
        print(f"👨‍🏫 Profesor creado: {user.get_full_name()}")
    return profesores
def crear_alumnos(curso):
    for _ in range(30):
        nombre = fake.first_name()
        apellido = fake.last_name()
        username = f"{nombre.lower()}.{apellido.lower()}{random.randint(1000, 9999)}"
        # print(f"Creando alumno: {username} ({nombre} {apellido}) en curso {curso.nombre}")
        user = User.objects.create_user(
            username=username[:150],  # asegurar límite
            password='test1234',
            first_name=nombre[:30],
            last_name=apellido[:30],
            rol='alumno',
            ci=str(fake.random_number(digits=10))[:20],
            telefono=fake.numerify(text="##########")[:20],
            genero=random.choice(['M', 'F', 'O']),  # correcto según tu modelo
            estado='activo'[:15]
        )

        Alumno.objects.create(
            usuario=user,
            codigo=f"AL{random.randint(1000,9999)}",
            fecha_nacimiento=fake.date_of_birth(minimum_age=10, maximum_age=18),
            direccion=fake.address(),
            curso=curso
        )
    print(f"👦🧒 30 alumnos creados para {curso.nombre}")

def crear_materias_y_evaluaciones(gestion, curso, profesores):
    materias_nivel = [
        'Matemáticas', 'Lenguaje', 'Física', 'Química',
        'Música', 'Psicología', 'Religión', 'Educación Física'
    ]
    trimestres = [1, 2, 3]
    dimensiones = ['ser', 'saber', 'hacer', 'decidir']
    tipos = ['examen', 'tarea', 'participacion']

    for nombre_materia in materias_nivel:
        profe = random.choice(profesores)
        materia = Materia.objects.create(
            nombre=nombre_materia,
            descripcion=f"Materia de {nombre_materia}",
            curso=curso,
            docente=profe,
            gestion=gestion
        )
        for t in trimestres:
            for i in range(3):
                Evaluacion.objects.create(
                    nombre=f"Eval {i+1} - T{t}",
                    tipo=random.choice(tipos),
                    dimension=random.choice(dimensiones),
                    porcentaje=random.choice([20, 25, 30]),
                    trimestre=t,
                    materia=materia,
                    gestion=gestion
                )
        print(f"📘 Materia creada: {nombre_materia} para {curso.nombre}")

def asignar_notas_y_asistencias(gestion, curso):
    alumnos = Alumno.objects.filter(curso=curso)
    materias = Materia.objects.filter(curso=curso, gestion=gestion)
    for materia in materias:
        evaluaciones = Evaluacion.objects.filter(materia=materia, gestion=gestion)
        for alumno in alumnos:
            for evaluacion in evaluaciones:
                NotaEvaluacion.objects.create(
                    evaluacion=evaluacion,
                    alumno=alumno,
                    nota=round(random.uniform(30, 100), 2)
                )
            for i in range(10):
                fecha = date(gestion.anio, 3, 1) + timedelta(days=i)
                Asistencia.objects.create(
                    alumno=alumno,
                    materia=materia,
                    gestion=gestion,
                    fecha=fecha,
                    presente=random.choice([True, True, False])
                )
    print(f"✅ Notas y asistencias asignadas para curso {curso.nombre}")

if __name__ == "__main__":
    print("🚀 Iniciando carga de datos para Gestión 2024...")
    gestion = crear_gestion(2024)
    cursos = crear_cursos()
    profesores = crear_profesores()
    for curso in cursos:
        crear_alumnos(curso)
        crear_materias_y_evaluaciones(gestion, curso, profesores)
        asignar_notas_y_asistencias(gestion, curso)
    print("🎉 Base de datos poblada correctamente con datos simulados de Gestión 2024.")
