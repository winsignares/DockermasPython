from flask import Blueprint, request, jsonify, json, Flask, render_template, redirect
#model
from Models.personas import Personas, PersonasSchema
from Config.db import db, ma, app

routes_UserC = Blueprint("routes_UserC",__name__) 

#modelos
persona_schema   = PersonasSchema()
personas_schemas = PersonasSchema(many=True)

@routes_UserC.route('/saveUser',methods=['POST'])
def saveUser():
    return "Datos Guardados"



@routes_UserC.route('/persona', methods=['GET'])
def clientes():
    resultall = Personas.query.all()
    resultPersona = personas_schemas.dump(resultall)
    return jsonify(resultPersona)