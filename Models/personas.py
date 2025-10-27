from Config.db import ma, db, app

class Personas(db.Model):
    __tablename__ = 'tblpersona'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre = nombre


class PersonaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Personas
        load_instance = True  

with app.app_context():
    db.create_all()
