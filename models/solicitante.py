from utils.db import db

class Solicitante(db.Model):
    id_solicitante = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(30))

    persona = db.relationship('Persona', backref='solicitante')

    def __init__(self, id_solicitante, id_persona, id_rol, telefono, correo):
        self.id_solicitante = id_solicitante
        self.id_persona = id_persona
        self.id_rol = id_rol
        self.telefono = telefono
        self.correo = correo
    
    @property
    def nombre_completo(self):
        if self.persona:
            return f"{self.persona.apellido_paterno} {self.persona.apellido_materno} {self.persona.nombres}"
        else:
            return "N/A"