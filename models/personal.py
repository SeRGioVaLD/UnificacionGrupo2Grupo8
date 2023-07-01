from utils.db import db

class Personal(db.Model):
    id_personal = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'))
    fecha_contrato = db.Column(db.Date)
    fecha_cese = db.Column(db.Date)

    persona = db.relationship('Persona', backref='personal')

    def __init__(self, id_personal, id_persona, id_rol, fecha_contrato, fecha_cese):
        self.id_personal = id_personal
        self.id_persona = id_persona
        self.id_rol = id_rol
        self.fecha_contrato = fecha_contrato
        self.fecha_cese = fecha_cese

    @property
    def nombre_completo(self):
        if self.persona:
            return f"{self.persona.apellido_paterno} {self.persona.apellido_materno} {self.persona.nombres}"
        else:
            return "N/A"