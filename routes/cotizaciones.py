from flask import Blueprint, render_template as rt, request, redirect, url_for
from models.solicitudCotizacion import SolicitudCotizacion
from models.solicitud import Solicitud
from models.predio import Predio
from models.solicitante import Solicitante
from models.personal import Personal
from models.estado import Estado
from models.servicio import Servicio  # Asegúrate de importar el modelo Servicio correctamente
from utils.db import db
from utils.id import formatear_id
from datetime import datetime

bp = Blueprint('cotizaciones', __name__, url_prefix="/cotizaciones")

@bp.route('/<id>/cotzac', methods=['POST','GET'])
def cotizaciones(id):
    # Obtener todas las solicitudes
    solicitudes = Solicitud.query.all()

    # Obtener todas las solicitudes con cotizaciones
    solicitudes_con_cotizaciones = SolicitudCotizacion.query.all()
    solicitudes_con_cotizaciones_ids = [cotizacion.id_solicitud for cotizacion in solicitudes_con_cotizaciones]
    
    # Obtener las solicitudes pendientes
    cotizaciones_pendientes = [solicitud for solicitud in solicitudes if solicitud.id_solicitud not in solicitudes_con_cotizaciones_ids]
    cotizaciones_completadas = SolicitudCotizacion.query.all()

    cotizaciones_pendientes = sorted(cotizaciones_pendientes, key=lambda solicitud: solicitud.id_solicitud)
    cotizaciones_completadas = sorted(cotizaciones_completadas, key=lambda solicitud: solicitud.id_solicitud)

    predios = Predio.query.all()
    predios_dict = {predio.id_predio: predio.descripcion for predio in predios}

    solicitantes = Solicitante.query.all()
    solicitantes_dict = {solicitante.id_solicitante: solicitante.nombre_completo for solicitante in solicitantes}

    servicios = Servicio.query.all()
    servicios_dict = {servicio.id_servicio: servicio.descripcion for servicio in servicios}

    personalAll = Personal.query.all()
    personal_dict = {personal.id_personal: personal.nombre_completo for personal in personalAll}
    
    estados = Estado.query.all()
    estado_dict = {estado.id_estado: estado.descripcion for estado in estados}

    for solicitudp in cotizaciones_pendientes:
        solicitudp.id_solicitud = formatear_id(solicitudp.id_solicitud)
        solicitudp.descripcion_predio = predios_dict.get(solicitudp.id_predio)
        solicitudp.nombre_solicitante = solicitantes_dict.get(solicitudp.id_solicitante)
        solicitudp.descripcion_servicio = servicios_dict.get(solicitudp.id_servicio)  # Obtener la descripción del servicio
    
    for solicitudc in cotizaciones_completadas:
        solicitudc.id_solicitud = formatear_id(solicitudc.id_solicitud)
        solicitudc.nombre_personal = personal_dict.get(solicitudc.id_personal)
        solicitudc.descripcion_estado = estado_dict.get(solicitudc.id_estado)
    bandera = ' '
    if request.method == "POST":
        bandera = request.form.get('btn-atras')
    return rt("cotizaciones.html", cotizaciones_pendientes=cotizaciones_pendientes, cotizaciones_completadas=cotizaciones_completadas, bandera=bandera, id = id)


@bp.route('/aceptar', methods=['POST'])
def aceptar():
    if request.method == "POST":
        #ID_SOLICITUD
        id_solicitud = request.form.get('aceptar__id_solicitud')
        solicitud = Solicitud.query.get(id_solicitud)
        servicio = Servicio.query.get(solicitud.id_servicio)
        estado = Estado.query.get(1)
        print("Aceptado: ",id_solicitud)
        #FECHA
        fecha_cotizacion = datetime.now().date()
        #ID_PERSONAL
        id_personal = 1
        #IMPORTE
        importe_total=0
        pago = {
            "adm": 500,
            "limp": 300,
            "jar": 300,
            "vig": 400,
        }
        if servicio.id_servicio == 1:
            total_adm = solicitud.cant_administracion*pago["adm"]
            total_lim = solicitud.cant_plimpieza*pago["limp"]
            total_jar = solicitud.cant_jardineria*pago["jar"]
            total_vig = solicitud.cant_vigilantes*pago["vig"]
            importe_total = total_adm+total_lim+total_jar+total_vig
        elif(servicio.id_servicio==2):
            total_lim = solicitud.cant_plimpieza*pago["limp"]
            importe_total = total_lim
        elif(servicio.id_servicio==3):
            total_jar = solicitud.cant_jardineria*pago["jar"]
            importe_total = total_jar
        elif(servicio.id_servicio==4):
            total_vig = solicitud.cant_vigilantes*pago["vig"]
            importe_total = total_vig
        new_solicitud_cotizacion = SolicitudCotizacion(id_solicitud,id_personal,fecha_cotizacion,importe_total,estado.id_estado)
        db.session.add(new_solicitud_cotizacion) # agregación
        db.session.commit() # confirmación
        return redirect(url_for('cotizaciones.cotizaciones'))

@bp.route('/rechazar', methods=['POST'])
def rechazar():
    if request.method == "POST":
        id_solicitud = request.form.get('rechazar__id_solicitud')
        print("Rechazado: ",id_solicitud)
        return redirect(url_for('cotizaciones.cotizaciones'))
