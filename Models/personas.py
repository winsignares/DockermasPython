from Config.db import ma, db, app

class Personas(db.Model):
    __tablename__ = 'tblpersona'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():
    db.create_all()

class PersonaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')