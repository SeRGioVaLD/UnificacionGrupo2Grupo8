from utils.db import db
class Servicio(db.Model):
    id_servicio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, id_servicio, descripcion):
        self.id_servicio = id_servicio
        self.descripcion = descripcion