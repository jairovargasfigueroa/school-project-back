from apps.alumnos.models import Alumno


def crear_Alumno(alumno_data):
    """
    Crea un nuevo alumno con los datos proporcionados.
    
    :param alumno_data: Diccionario con los datos del alumno.
    :return: Instancia del alumno creado.
    """
    return Alumno.objects.create(**alumno_data)

def actualizar_Alumno(alumno, alumno_data):
    """
    Actualiza un alumno existente con los nuevos datos proporcionados.
    
    :param alumno: Instancia del alumno a actualizar.
    :param alumno_data: Diccionario con los nuevos datos del alumno.
    :return: Instancia del alumno actualizado.
    """
    for attr, value in alumno_data.items():
        setattr(alumno, attr, value)
    alumno.save()
    return alumno

def eliminar_Alumno(alumno):
    """
    Elimina un alumno existente.
    
    :param alumno: Instancia del alumno a eliminar.
    :return: None
    """
    alumno.delete()

def obtener_Alumno_por_id(alumno_id):
    """
    Obtiene un alumno por su ID.
    
    :param alumno_id: ID del alumno a buscar.
    :return: Instancia del alumno encontrado o None si no existe.
    """
    try:
        return Alumno.objects.get(id=alumno_id)
    except Alumno.DoesNotExist:
        return None        
    