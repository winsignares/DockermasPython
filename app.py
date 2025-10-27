from flask import Flask, request, jsonify, redirect, session, render_template, abort
from Config.db import app
import secrets 

from Config.Controller.UserController import routes_UserC

app.register_blueprint(routes_UserC, url_prefix="/controller")



@app.route("/")
def index():
    return "Hola Mundo Web"

@app.route("/main")
def main():
    return render_template("views/dashboard.html")

@app.route("/tablas")
def tablas():
    empleados = [
        {"name": "Tiger Nixon", "position": "System Architect", "office": "Edinburgh", "age": 61, "start_date": "2011/04/25", "salary": "$320,800"},
        {"name": "Garrett Winters", "position": "Accountant", "office": "Tokyo", "age": 63, "start_date": "2011/07/25", "salary": "$170,750"},
        {"name": "Ashton Cox", "position": "Junior Technical Author", "office": "San Francisco", "age": 66, "start_date": "2009/01/12", "salary": "$86,000"},
        {"name": "Cedric Kelly", "position": "Senior Javascript Developer", "office": "Edinburgh", "age": 22, "start_date": "2012/03/29", "salary": "$433,060"},
        {"name": "Airi Satou", "position": "Accountant", "office": "Tokyo", "age": 33, "start_date": "2008/11/28", "salary": "$162,700"},
        {"name": "Brielle Williamson", "position": "Integration Specialist", "office": "New York", "age": 61, "start_date": "2012/12/02", "salary": "$372,000"},
        {"name": "Herrod Chandler", "position": "Sales Assistant", "office": "San Francisco", "age": 59, "start_date": "2012/08/06", "salary": "$137,500"}
    ]
    return render_template("views/tables.html", empleados=empleados)

@app.route("/cargarTabla")
def cargarTabla():
    empleados = [
        {"name": "Tiger Nixon", "position": "System Architect", "office": "Edinburgh", "age": 61, "start_date": "2011/04/25", "salary": "$320,800"},
        {"name": "Garrett Winters", "position": "Accountant", "office": "Tokyo", "age": 63, "start_date": "2011/07/25", "salary": "$170,750"},
        {"name": "Ashton Cox", "position": "Junior Technical Author", "office": "San Francisco", "age": 66, "start_date": "2009/01/12", "salary": "$86,000"},
        {"name": "Cedric Kelly", "position": "Senior Javascript Developer", "office": "Edinburgh", "age": 22, "start_date": "2012/03/29", "salary": "$433,060"},
        {"name": "Airi Satou", "position": "Accountant", "office": "Tokyo", "age": 33, "start_date": "2008/11/28", "salary": "$162,700"},
        {"name": "Brielle Williamson", "position": "Integration Specialist", "office": "New York", "age": 61, "start_date": "2012/12/02", "salary": "$372,000"},
        {"name": "Herrod Chandler", "position": "Sales Assistant", "office": "San Francisco", "age": 59, "start_date": "2012/08/06", "salary": "$137,500"}
    ]
    return empleados

@app.route("/login")
def login():
    token = generete_csrf_token()
    return render_template("views/login.html", csrf_token = token)


def generete_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_urlsafe(32)
    return session['csrf_token']

def validar_csrf(token_from_request):
    token_session = session.get('csrf_token')
    return token_session and secrets.compare_digest(token_session, token_from_request or "")

@app.route("/submit", methods=['POST'])
def submit():
    token = request.headers.get('X-CSRF-Token') or request.form.get('csrf_token')
    if not validar_csrf(token):
        abort(403, description="CSRF Token Invalido")
    data = request.form.to_dict()
    if data['exampleInputEmail'] == "aaa@aaa.com" and data['exampleInputPassword'] == "123":
        return jsonify({
            "status": 200,
            "url":"/tablas"
        })   
    else:
        return jsonify({
            "status": 200,
            "received":data
        }) 




if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')