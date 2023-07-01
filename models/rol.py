from utils.db import db

class Rol(db.Model):
    id_rol = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(60))
    def __init__(self, id_rol, descripcion):
        self.id_rol = id_rol
        self.descripcion = descripcion