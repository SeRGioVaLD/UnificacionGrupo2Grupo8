from utils.db import db

class Ubigeo(db.Model):
    idubigeo = db.Column(db.String(6), primary_key=True)
    departamento = db.Column(db.String(60))
    provincia = db.Column(db.String(60))
    distrito = db.Column(db.String(60))
    superficie = db.Column(db.Numeric(10, 4))
    altitud = db.Column(db.Numeric(10, 4))
    latitud = db.Column(db.Numeric(10, 4))
    longitud = db.Column(db.Numeric(10, 4))

    def __init__(self, idubigeo, departamento, provincia, distrito, superficie, altitud, latitud, longitud):
        self.idubigeo = idubigeo
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.superficie = superficie
        self.altitud = altitud
        self.latitud = latitud
        self.longitud = longitud