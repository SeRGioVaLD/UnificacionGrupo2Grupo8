from utils.db import db

class Area_Comun(db.Model):
    __tablename__ = 'area_comun'
    id_area_comun = db.Column(db.Integer(), primary_key = True)
    descripcion = db.Column(db.String(50)) 