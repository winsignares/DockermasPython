from flask import Blueprint, request, jsonify
from Models.personas import Personas, PersonaSchema
from Config.db import db, ma, app

routes_UserC = Blueprint("routes_UserC", __name__)

# Esquemas de serialización
persona_schema = PersonaSchema()
personas_schemas = PersonaSchema(many=True)


@routes_UserC.route('/persona', methods=['POST'])
def saveUser():
    nombre = request.json['nombre']    

    if not nombre :
        return jsonify({"error": "Faltan campos requeridos"}), 400

    new_persona = Personas(nombre=nombre)
    db.session.add(new_persona)
    db.session.commit()

    return persona_schema.jsonify(new_persona), 201



@routes_UserC.route('/persona', methods=['GET'])
def getPersonas():
    all_personas = Personas.query.all()
    result = personas_schemas.dump(all_personas)
    return jsonify(result)



@routes_UserC.route('/persona/<int:id>', methods=['GET'])
def getPersona(id):
    persona = Personas.query.get(id)
    if not persona:
        return jsonify({"message": "Persona no encontrada"}), 404
    return persona_schema.jsonify(persona)


@routes_UserC.route('/persona/<int:id>', methods=['PUT'])
def updatePersona(id):
    persona = Personas.query.get(id)
    if not persona:
        return jsonify({"message": "Persona no encontrada"}), 404

    nombre = request.json.get('nombre', persona.nombre)
    
    persona.nombre = nombre
    db.session.commit()
    return persona_schema.jsonify(persona)


@routes_UserC.route('/persona/<int:id>', methods=['DELETE'])
def deletePersona(id):
    persona = Personas.query.get(id)
    if not persona:
        return jsonify({"message": "Persona no encontrada"}), 404

    db.session.delete(persona)
    db.session.commit()
    return jsonify({"message": "Persona eliminada correctamente"}), 200
