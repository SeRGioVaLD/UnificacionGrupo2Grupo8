from flask import Blueprint, render_template as rt, flash, redirect, url_for, request, jsonify
from models.persona import Persona
from models.personal import Personal
from models.predio import Predio
from models.rol import Rol
from models.servicio import Servicio
from models.solicitante import Solicitante
from models.solicitud import Solicitud
from models.solicitudCotizacion import SolicitudCotizacion
from models.tipoDocumento import TipoDocumento
from models.tipoPredio import TipoPredio
from models.ubigeo import Ubigeo

from utils.db import db
from utils.json import model_to_dict

bp = Blueprint('vista', __name__, url_prefix="/vista") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def vista(): #esta función debe coincidir con el url_for del html (base)
    persona =Persona.query.all()
    personal =Personal.query.all()
    predio =Predio.query.all()
    rol =Rol.query.all()
    servicio =Servicio.query.all()
    solicitante =Solicitante.query.all()
    solicitud =Solicitud.query.all()
    solicitudCotizacion =SolicitudCotizacion.query.all()
    tipoDocumento =TipoDocumento.query.all()
    tipoPredio =TipoPredio.query.all()
    ubigeo =Ubigeo.query.all()

    data_persona = []
    data_personal = []
    data_predio = []
    data_rol = []
    data_servicio = []
    data_solicitante = []
    data_solicitud = []
    data_solicitudCotizacion = []
    data_tipoDocumento = []
    data_tipoPredio = []
    data_ubigeo = []

    # Crear una lista para almacenar los datos convertidos a json
    for obj in persona:
        x = model_to_dict(obj)
        data_persona.append(x)
    for obj in personal:
        x = model_to_dict(obj)
        data_personal.append(x)
    for obj in predio:
        x = model_to_dict(obj)
        data_predio.append(x)
    for obj in rol:
        x = model_to_dict(obj)
        data_rol.append(x)
    for obj in servicio:
        x = model_to_dict(obj)
        data_servicio.append(x)
    for obj in solicitante:
        x = model_to_dict(obj)
        data_solicitante.append(x)
    for obj in solicitud:
        x = model_to_dict(obj)
        data_solicitud.append(x)
    for obj in solicitudCotizacion:
        x = model_to_dict(obj)
        data_solicitudCotizacion.append(x)
    for obj in tipoDocumento:
        x = model_to_dict(obj)
        data_tipoDocumento.append(x)
    for obj in tipoPredio:
        x = model_to_dict(obj)
        data_tipoPredio.append(x)
    for obj in ubigeo:
        data_ubigeo=model_to_dict(obj)
    
    result = {
        'persona': data_persona,
        'personal': data_personal,
        'predio': data_predio,
        'rol': data_rol,
        'servicio': data_servicio,
        'solicitante': data_solicitante,
        'solicitud': data_solicitud,
        'solicitudCotizacion': data_solicitudCotizacion,
        'tipoDocumento': data_tipoDocumento,
        'tipoPredio': data_tipoPredio,
        'ubigeo': data_ubigeo
    }

    return jsonify(result)

@bp.route('/predio')
def vista_predio():
    query =Predio.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'predio': data
    }
    return jsonify(result)

@bp.route('/tipo_predio')
def vista_tipo_predio():
    query =TipoPredio.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'tipo_predio': data
    }
    return jsonify(result)

@bp.route('/persona')
def vista_persona():
    query =Persona.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'persona': data
    }
    return jsonify(result)

@bp.route('/personal')
def vista_personal():
    query =Personal.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'personal': data
    }
    return jsonify(result)

@bp.route('/solicitante')
def vista_solicitante():
    query =Solicitante.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'solicitante': data
    }
    return jsonify(result)

@bp.route('/servicio')
def vista_servicio():
    query =Servicio.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'servicio': data
    }
    return jsonify(result)

@bp.route('/rol')
def vista_rol():
    query =Rol.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'rol': data
    }
    return jsonify(result)

@bp.route('/solicitud')
def vista_solicitud():
    query =Solicitud.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'solicitud': data
    }
    return jsonify(result)

@bp.route('/solicitud_cotizacion')
def vista_solicitud_cotizacion():
    query =SolicitudCotizacion.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'solicitud_cotizacion': data
    }
    return jsonify(result)

""" @bp.route("/update_predio/<string:id_predio>", methods=["GET", "POST"])
def update_predio(id_predio):
    # Obtener la data correspondiente al id recibido como argumento
    predio = Predio.query.get(id_predio)

    if request.method == "POST":
        # Obtener los nuevos datos del predio desde el formulario y actualizarlos en la base de datos
        predio.area = request.form['update_area']
        predio.areas_comunes = request.form['update_areascomunes']
        predio.NroPuertasAcceso = request.form['update_NroPuertasAcceso']
        predio.NroHabitaciones = request.form['update_NroHabitaciones']
        db.session.commit()

        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Contact updated successfully!')

        # Redirigir a la página principal
        return redirect(url_for('vista.vista'))

    # Renderizar la página de actualización
    return rt("update_predio.html", predio=predio)

@bp.route("/update_representante/<string:id_representante>", methods=["GET", "POST"])
def update_representante(id_representante):
    # Obtener la data correspondiente al id recibido como argumento
    representante = PresidentePredio.query.get(id_representante)

    if request.method == "POST":
        # Obtener los nuevos datos del predio desde el formulario y actualizarlos en la base de datos
        representante.dni = request.form['update_documento']
        representante.apellidos = request.form['update_apellidos']
        representante.nombres = request.form['update_nombres']
        representante.predio_asignado = request.form['update_predio']
        representante.telefono = request.form['update_telefono']
        representante.correo = request.form['update_correo']
        db.session.commit()

        # Mostrar un mensaje de éxito en la siguiente petición
        flash('Contact updated successfully!')

        # Redirigir a la página principal
        return redirect(url_for('vista.vista'))

    # Renderizar la página de actualización
    return rt("update_representante.html", representante=representante)

@bp.route('/delete/<int:id_representante>/<int:id_predio>/<int:id_contrato>')
def delete(id_representante, id_predio, id_contrato):
    # Obtener el contacto correspondiente al id recibido como argumento
    predio= Predio.query.get(id_predio)
    representante= PresidentePredio.query.get(id_representante)
    contrato= Contrato.query.get(id_contrato)

    # Eliminar el contacto de la base de datos y confirmar la operación
    db.session.delete(representante)
    db.session.commit()
    db.session.delete(contrato)
    db.session.delete(predio)
    db.session.commit()
    # Mostrar un mensaje de éxito en la siguiente petición
    flash('Datos eliminados correctamente!')

    # Redirigir a la página principal
    return redirect(url_for('vista.vista')) """