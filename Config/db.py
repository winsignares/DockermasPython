from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '12345')
DB_HOST = os.getenv('DB_HOST', 'mysql')  
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'mysql')


app = Flask(__name__)
#creamos las credenciales para conectarnos a la bd
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "web"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#creamos los objetos de bd

db = SQLAlchemy(app)
ma = Marshmallow(app)

