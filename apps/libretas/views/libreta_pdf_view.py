from django.views import View
from django.http import FileResponse, HttpResponse
from apps.usuarios.models import Alumno
from apps.gestiones.models import Gestion
from apps.libretas.services.libreta_service import generar_libreta
from apps.libretas.services.libreta_pdf_service import generar_pdf_libreta


class LibretaPDFView(View):
    
    def get(self, request, alumno_id, gestion_id):
        try:
            alumno = Alumno.objects.get(id=alumno_id)
            gestion = Gestion.objects.get(id=gestion_id)
            print(f"Generando libreta para alumno: {alumno_id}, gestión: {gestion_id}")
            libreta_data = generar_libreta(alumno, gestion)
            print(f"Datos de la libreta generados: {libreta_data}")
            if not libreta_data:
                return HttpResponse("No se pudo generar la libreta", status=500, content_type='text/plain')
            
            pdf_file = generar_pdf_libreta(libreta_data)
            print(f"PDF generado: {pdf_file}")
            response = FileResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename=libreta_{alumno.id}_{gestion.anio}.pdf'
            return response

        except Alumno.DoesNotExist:
            return HttpResponse("Alumno no encontrado", status=404, content_type='text/plain')
        except Gestion.DoesNotExist:
            return HttpResponse("Gestión no encontrada", status=404, content_type='text/plain')


# from django.views import View
# from django.http import FileResponse, HttpResponse
# from apps.usuarios.models import Alumno
# from apps.gestiones.models import Gestion
# from apps.libretas.services.libreta_service import generar_libreta
# from apps.libretas.services.libreta_pdf_service import generar_pdf_libreta


# class LibretaPDFView(View):
    
#     def get(self, request, alumno_id, gestion_id):
#         try:
#             alumno = Alumno.objects.get(id=alumno_id)
#             gestion = Gestion.objects.get(id=gestion_id)

#             libreta_data = generar_libreta(alumno, gestion)
#             if not libreta_data:
#                 return HttpResponse("No se pudo generar la libreta", status=500, content_type='text/plain')
            
#             pdf_file = generar_pdf_libreta(libreta_data)

#             # response = FileResponse(pdf_file, content_type='application/pdf')
#             # 👇 Forzar descarga
#             # response['Content-Disposition'] = f'attachment; filename=libreta_{alumno.id}_{gestion.anio}.pdf'
#             # return response

#             # response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#             # response['Content-Disposition'] = f'attachment; filename=libreta_{alumno.id}_{gestion.anio}.pdf'
#              # 🟢 Opción 1: Descargar automáticamente
#             response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#             response['Content-Disposition'] = f'attachment; filename=libreta_{alumno.id}_{gestion.anio}.pdf'
#             return response  # <<<< ¡ESTO FALTABA!
#         except Alumno.DoesNotExist:
#             return HttpResponse("Alumno no encontrado", status=404, content_type='text/plain')
#         except Gestion.DoesNotExist:
#             return HttpResponse("Gestión no encontrada", status=404, content_type='text/plain')
