
from apps.evaluaciones.models import Evaluacion
from apps.materias.models import Materia
from apps.notas.models import NotaEvaluacion


PONDERACION_DIMENSION = {
    'ser': 0.1,
    'saber': 0.4,
    'hacer': 0.3,
    'decidir': 0.2
}

def calcular_nota_trimestre(alumno, materia, gestion, trimestre):
    evaluaciones = Evaluacion.objects.filter(
        materia=materia,
        gestion=gestion,
        trimestre=trimestre
    )
    acumulado = {dim: {'total': 0, 'nota': 0} for dim in PONDERACION_DIMENSION}

    for evaluacion in evaluaciones:
        nota = NotaEvaluacion.objects.filter(alumno=alumno, evaluacion=evaluacion).first()
        if nota:
            dim = evaluacion.dimension
            acumulado[dim]['nota'] += float(nota.nota) * float(evaluacion.porcentaje)
            acumulado[dim]['total'] += float(evaluacion.porcentaje)

    nota_final = 0
    for dim, valores in acumulado.items():
        if valores['total'] > 0:
            promedio = valores['nota'] / valores['total']
            nota_final += promedio * PONDERACION_DIMENSION[dim]

    return round(nota_final, 2)

def calcular_nota_materia_gestion(alumno, materia, gestion):
    total = 0
    for t in [1, 2, 3]:
        total += calcular_nota_trimestre(alumno, materia, gestion, t)
    return round(total / 3, 2)

def calcular_promedio_general_gestion(alumno, gestion):
    materias = Materia.objects.filter(curso=alumno.curso, gestion=gestion)
    total = 0
    count = 0
    for materia in materias:
        total += calcular_nota_materia_gestion(alumno, materia, gestion)
        count += 1
    return round(total / count, 2) if count > 0 else 0

def generar_libreta(alumno, gestion):
    materias = Materia.objects.filter(curso=alumno.curso, gestion=gestion)
    data = []

    for materia in materias:
        notas_trimestre = [
            calcular_nota_trimestre(alumno, materia, gestion, t) for t in [1, 2, 3]
        ]
        nota_final = round(sum(notas_trimestre) / 3, 2)
        data.append({
            "materia": materia.nombre,
            "trimestre_1": notas_trimestre[0],
            "trimestre_2": notas_trimestre[1],
            "trimestre_3": notas_trimestre[2],
            "nota_final": nota_final
        })

    promedio_general = calcular_promedio_general_gestion(alumno, gestion)

    return {
        "alumno": alumno.usuario.get_full_name(),
        "gestion": gestion.anio,
        "promedio_general": promedio_general,
        "detalle": data
    }
