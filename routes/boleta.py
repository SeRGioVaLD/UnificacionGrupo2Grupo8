from flask import Blueprint
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from flask import make_response, request
from utils.id import formatear_id

from models.solicitud import Solicitud
from models.solicitante import Solicitante
from models.persona import Persona
from models.rol import Rol
from models.predio import Predio
from models.tipoPredio import TipoPredio
from models.servicio import Servicio
from models.solicitudCotizacion import SolicitudCotizacion

bp = Blueprint('boleta', __name__, url_prefix="/boleta") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/', methods=['POST'])
def generar_pdf():
    # Crear un objeto de lienzo PDF
    buffer = BytesIO()  # Crear un buffer de bytes para almacenar el PDF generado
    pdf = canvas.Canvas(buffer)
    
    id_solicitud = request.form.get('descargar__id_solicitud')

    titulo = f"Cotizacion - {formatear_id(id_solicitud)}"

    pdf.setTitle(titulo)

    dibujar_encabezado(pdf,50,600)
    dibujar_body(pdf,id_solicitud,100,510)
    dibujar_footer(pdf,50,50)

    pdf.setPageSize((600, 650))  # Establecer un ancho de 500 puntos y un alto de 700 puntos
    # Guardar el lienzo y finalizar el PDF
    pdf.save()

    buffer.seek(0)  # Restablecer el puntero del buffer al principio
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={titulo}.pdf'
    return response

# ENCABEZADO
def dibujar_encabezado(pdf,x_encabezado,y_encabezado):
    # Definir las coordenadas para el encabezado y la línea
    x_linea = 50  # posición x de la línea
    y_linea = y_encabezado - 10  # posición y de la línea (ajusta la separación)
    # Configurar la fuente y el tamaño del texto del encabezado
    pdf.setFont("Helvetica-Bold", 18)
    # Dibujar el encabezado
    pdf.drawString(x_encabezado, y_encabezado, "CONDOSA S.A.")
    # Dibujar la línea
    pdf.setLineWidth(5)  # grosor de la línea
    pdf.setStrokeColorRGB(4/255, 26/255, 47/255) 
    pdf.line(x_linea, y_linea, pdf._pagesize[0] - x_linea, y_linea)  # dibujar línea horizontal

# BODY
def dibujar_body(pdf,id_solicitud,posicionx,posiciony):
    data = obtener_data(id_solicitud)
    generar_titulo(pdf,data,posicionx+50,posiciony) #Título en posicion 100, 740
    generar_infoSolicitante(pdf,data,posicionx,posiciony-60)
    generar_tabla(pdf,data,posicionx,posiciony-160)

def generar_titulo(pdf,data,xtitulo,ytitulo):
    #titulo en sí -> 100,740
    pdf.setFont("Helvetica-Bold", 25)
    pdf.drawString(xtitulo, ytitulo, "COTIZACION DE SERVICIOS")
    #id -> 100,725  
    pdf.setFont("Helvetica", 10)
    pdf.drawString(xtitulo, ytitulo-15, f"Id-Solicitud: {formatear_id(data['id_solicitud'])}")
    #fecha -> 400, 725
    pdf.drawString(xtitulo+250, ytitulo-15, f"Fecha: {data['fecha']}")

def generar_infoSolicitante(pdf,data,posix,posiy):
    # Obtener datos del solicitante
    nombre = data["nombres_apellido"]
    nro_documento = data["ndocumento"]
    predio = data["nombre_predio"]
    ruc = data["ruc_predio"]
    cargo = data["rol"]
    correo = data["correo"]
    telefono = data["telefono"]
    
    pdf.setFont("Helvetica-BoldOblique", 10)
    pdf.drawString(posix, posiy+15, "Solicitante")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(posix, posiy, "Nombre:")
    pdf.drawString(posix, posiy-20, "Nro documento:")
    pdf.drawString(posix, posiy-40, "Predio:")
    pdf.drawString(posix, posiy-60, "R.U.C.:")
    pdf.drawString(posix+200, posiy, "Rol:")
    pdf.drawString(posix+200, posiy-20, "Correo:")
    pdf.drawString(posix+200, posiy-40, "Telefono:")
    pdf.setFillColor(colors.black)  # Restablecer color negro para los siguientes textos
    pdf.drawString(posix+70, posiy, nombre)
    pdf.drawString(posix+90, posiy-20, nro_documento) 
    pdf.drawString(posix+70, posiy-40, predio)
    pdf.drawString(posix+70, posiy-60, ruc)
    pdf.drawString(posix+270, posiy, cargo)
    pdf.drawString(posix+270, posiy-20, correo)
    pdf.drawString(posix+270, posiy-40, str(telefono))

#generar tabla del body
def generar_tabla(pdf,data,posix,posiy):
    administracion =False
    # Tus cuatro listas con valores unitarios
    lista1 = [data["id_servicio"]]
    lista2 = [data["tipo_servicio"]]
    if data["id_servicio"] == 1:
        data["cantidad_total"]=data["cant_administracion"]
        data["importe_total"]=data["importe_administracion"]*data["cantidad_total"]
        administracion=True
    elif(data["id_servicio"]==2):
        data["cantidad_total"]=data["cant_plimpieza"]
        data["importe_total"]=data["importe_plimpieza"]*data["cantidad_total"]
    elif(data["id_servicio"]==3):
        data["cantidad_total"]=data["cant_jardineria"]
        data["importe_total"]=data["importe_jardineria"]*data["cantidad_total"]
    elif(data["id_servicio"]==4):
        data["cantidad_total"]=data["cant_vigilantes"]
        data["importe_total"]=data["importe_vigilantes"]*data["cantidad_total"]

    lista3 = [data["cantidad_total"]]
    lista4 = [data["importe_total"]]
    
    if administracion:
        if(data["cant_plimpieza"]!=0):
            lista1.append("2")
            lista2.append("Limpieza")
            lista3.append(data["cant_plimpieza"])
            lista4.append(data["importe_plimpieza"]*data["cant_plimpieza"])
        if(data["cant_jardineria"]!=0):
            lista1.append("3")
            lista2.append("Jardinería")
            lista3.append(data["cant_jardineria"])
            lista4.append(data["importe_jardineria"]*data["cant_jardineria"])
        if(data["cant_vigilantes"]!=0):
            lista1.append("4")
            lista2.append("Vigilancia")
            lista3.append(data["cant_vigilantes"])
            lista4.append(data["importe_vigilantes"]*data["cant_vigilantes"])
    
    # Combina las listas utilizando zip()
    data = zip(lista1, lista2, lista3, lista4)
    # Construye la estructura de datos para la tabla
    table_data = [
        ['Nro Servicio', 'Descripción', 'Cantidad', 'Monto (S/)'],  # Nombres de las columnas
    ]
    # Agrega las filas de datos a la estructura de la tabla
    for row in data:
        table_data.append(list(row))

    table_data.append(["","","Monto Neto",round(sum(lista4)*100/118,2)])
    table_data.append(["","","IGV (18%)",round(sum(lista4)*(100/118)*(18/100),2)])
    table_data.append(["","","Monto Total",sum(lista4)])
    color_azul = ((4/255, 26/255, 47/255))
    color_azulclaro = ((215/255, 235/255, 255/255))
    table = Table(table_data, colWidths=100, rowHeights=30)
    estilo_tabla = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), color_azul),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('GRID', (0, 0), (-1, -4), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, -1), 11),
    ])
    # Alternar colores de fondo para filas
    for i in range(1, len(table_data)):
        if i % 2 == 0 and i!=0:
            estilo_tabla.add('BACKGROUND', (0, i), (-1, i), colors.white)
        else:
            estilo_tabla.add('BACKGROUND', (0, i), (-1, i), color_azulclaro)
    # Negrita en el total
    for i in range(1, len(table_data)):
        if i >= len(table_data)-3:
            estilo_tabla.add('BACKGROUND', (0, i), (-3, i), colors.white),
            estilo_tabla.add('GRID', (0, i), (-3, i), 0, colors.white),
            estilo_tabla.add('GRID', (2, i), (-1, -1), 1, colors.black),
        if i == len(table_data)-3:
            estilo_tabla.add('GRID', (0, i-1), (-3, i-1), 1, colors.black),
    # Negrita en el total
    for i in range(1, len(table_data)):
        if i >= len(table_data)-3:
            estilo_tabla.add('FONTNAME', (2, i), (-2, i), 'Helvetica-Bold'),
    table.setStyle(estilo_tabla)
    table.wrapOn(pdf, 400, 500)
    pdf.setFont("Helvetica-BoldOblique", 10)
    pdf.drawString(posix, posiy+5, "Cotización")
    table.drawOn(pdf, posix, posiy-table._height)

#obtener la data para imprimirla
def obtener_data(id_solicitud):
    solicitud = Solicitud.query.get(id_solicitud)
    solicitante = Solicitante.query.get(solicitud.id_solicitante)
    persona = Persona.query.get(solicitante.id_persona)
    rol = Rol.query.get(solicitante.id_rol)
    predio = Predio.query.get(solicitud.id_predio)
    tipo_predio = TipoPredio.query.get(predio.id_tipo_predio)
    servicio = Servicio.query.get(solicitud.id_servicio)
    solicitud_cotizacion = SolicitudCotizacion.query.get(solicitud.id_solicitud)

    data = {
        "id_solicitud": solicitud.id_solicitud,
        "id_solicitante": solicitud.id_solicitante,
        "id_predio": solicitud.id_predio,
        "id_servicio": solicitud.id_servicio,
        "id_persona": solicitante.id_persona,
        "id_tipo_predio": predio.id_tipo_predio,
        #informacion personal
        "nombres_apellido": persona.nombres + " " + persona.apellido_paterno,
        "ndocumento": persona.ndocumento,
        "rol": rol.descripcion,
        "correo": solicitante.correo,
        "telefono": solicitante.telefono,
        #informacion del predio
        "nombre_predio": predio.descripcion,
        "direccion_predio": predio.direccion,
        "tipo_predio": tipo_predio.nomre_predio,
        "ruc_predio": predio.ruc,
        #informacion de los servicios
        "tipo_servicio": servicio.descripcion,
        "cant_administracion": solicitud.cant_administracion,
        "cant_plimpieza": solicitud.cant_plimpieza,
        "cant_jardineria": solicitud.cant_jardineria,
        "cant_vigilantes": solicitud.cant_vigilantes,
        "importe_administracion": 500,
        "importe_plimpieza" : 300,
        "importe_jardineria": 300,
        "importe_vigilantes": 400,
        "cantidad_total": 0,
        "fecha": solicitud_cotizacion.fecha_cotizacion,
    }
    return data

# FOOTER
def dibujar_footer(pdf,x_footer,y_footer):
    pdf.setFont("Helvetica-Bold", 10)
    # Definir las coordenadas para el footer y la línea
    x_linea = x_footer  # posición x de la línea
    y_linea = y_footer + 20  # posición y de la línea (ajusta la separación)
    # Dibujar una línea negra encima del footer
    pdf.setLineWidth(5)  # Establecer el ancho de línea
    pdf.setStrokeColorRGB(4/255, 26/255, 47/255)  
    pdf.line(x_linea, y_linea, pdf._pagesize[0] - x_linea, y_linea)  # dibujar línea horizontal
    # Agregar texto al lienzo
    pdf.drawString(x_footer, y_footer, "\u00A9 2023 CONDOSA. Todos los derechos reservados.")