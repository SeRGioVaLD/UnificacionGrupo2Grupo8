from utils.db import db

class Estado(db.Model):
    id_estado = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(60))
    def __init__(self, id_estado, descripcion):
        self.id_estado = id_estado
        self.descripcion = descripcion