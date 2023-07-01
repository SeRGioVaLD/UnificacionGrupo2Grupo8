from utils.db import db
        
class Contrato(db.Model):
    __tablename__ = 'contrato'
    id_contrato = db.Column(db.Integer(), primary_key=True)
    id_personal = db.Column(db.Integer())
    id_solicitante = db.Column(db.Integer())
    id_solicitud_cotizacion = db.Column(db.Integer())
    fecha_contrato = db.Column(db.Date())
    fecha_firma_solicitante = db.Column(db.Date())
    fecha_firma_personal = db.Column(db.Date())
    fecha_registro = db.Column(db.Date())
    minuta = db.Column(db.String(100))

    def __init__(self, id_solicitud_cotizacion, id_personal, id_solicitante, fecha_contrato, fecha_firma_solicitante, fecha_firma_personal, fecha_registro, minuta):
        self.id_solicitud_cotizacion = id_solicitud_cotizacion
        self.id_personal = id_personal
        self.id_solicitante = id_solicitante
        self.fecha_contrato = fecha_contrato
        self.fecha_firma_solicitante = fecha_firma_solicitante
        self.fecha_firma_personal = fecha_firma_personal
        self.fecha_registro = fecha_registro
        self.minuta = minuta
        
#action="{{url_for('routes.crear_contrato',id = cotizacion.id_personal, id_solicitud_cotizacion = cotizacion.id_solicitud_cotizacion)}}" method="POST"