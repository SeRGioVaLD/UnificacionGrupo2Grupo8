from utils.db import db

class Predio_Area_Comun(db.Model):
    __tablename__ = 'predio_area_comun'
    id_predio = db.Column(db.Integer(), primary_key = True)
    id_area_comun = db.Column(db.Integer(), primary_key = True)
    codigo = db.Column(db.String(6))
    area = db.Column(db.Float())