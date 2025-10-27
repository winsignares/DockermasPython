from flask import Blueprint, request, jsonify, json, Flask, render_template, redirect
#model

from Config.db import db, ma, app

routes_UserC = Blueprint("routes_UserC",__name__) 

#modelos

@routes_UserC.route('/saveUser',methods=['POST'])
def saveUser():
    return "Datos Guardados"