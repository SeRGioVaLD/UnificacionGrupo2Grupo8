from utils.db import db

class SolicitudCotizacion(db.Model):
    id_solicitud = db.Column(db.Integer)
    id_personal = db.Column(db.Integer, db.ForeignKey('personal.id_personal'))
    fecha_cotizacion = db.Column(db.Date)
    importe = db.Column(db.DECIMAL(6, 2))
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'))
    id_solicitud_cotizacion = db.Column(db.Integer, primary_key=True)
    def __init__(self, id_solicitud, id_personal, fecha_cotizacion, importe,id_estado):
        self.id_solicitud = id_solicitud
        self.id_personal = id_personal
        self.fecha_cotizacion = fecha_cotizacion
        self.importe = importe
        self.id_estado = id_estado