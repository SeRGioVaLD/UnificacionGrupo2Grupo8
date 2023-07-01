from utils.db import db

class TipoDocumento(db.Model):
    id_tipo_documento = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20))

    def __init__(self, id_tipo_documento, descripcion):
        self.id_tipo_documento = id_tipo_documento
        self.descripcion = descripcion