# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# from reportlab.lib.pagesizes import A4
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from io import BytesIO



# def generar_pdf_libreta(data):
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=A4)
#     elements = []
#     styles = getSampleStyleSheet()

#     elements.append(Paragraph(f"Libreta de: {data['alumno']}", styles['Heading2']))
#     elements.append(Paragraph(f"Gestión: {data['gestion']}", styles['Normal']))
#     elements.append(Spacer(1, 12))

#     table_data = [["Materia", "Trimestre 1", "Trimestre 2", "Trimestre 3", "Nota Final"]]
#     for item in data["detalle"]:
#         table_data.append([
#             item["materia"],
#             item["trimestre_1"],
#             item["trimestre_2"],
#             item["trimestre_3"],
#             item["nota_final"]
#         ])

#     table = Table(table_data, hAlign='LEFT')
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
#     ]))
#     elements.append(table)
#     elements.append(Spacer(1, 12))
#     elements.append(Paragraph(f"Promedio General: {data['promedio_general']}", styles['Heading3']))

#     doc.build(elements)
#     buffer.seek(0)
#     return buffer


from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def generar_pdf_libreta(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"Libreta de: {data['alumno']}", styles['Heading2']))
    elements.append(Paragraph(f"Gestión: {data['gestion']}", styles['Normal']))
    elements.append(Spacer(1, 12))

    table_data = [["Materia", "Trimestre 1", "Trimestre 2", "Trimestre 3", "Nota Final"]]
    for item in data["detalle"]:
        table_data.append([
            item["materia"],
            item["trimestre_1"],
            item["trimestre_2"],
            item["trimestre_3"],
            item["nota_final"]
        ])

    table = Table(table_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Promedio General: {data['promedio_general']}", styles['Heading3']))

    doc.build(elements)
    buffer.seek(0)
    return buffer
