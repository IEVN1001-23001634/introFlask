from flask import Flask, jsonify, request,Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp
from blueprints import registrar_blueprints

from config import config

app = Flask(__name__)

CORS(app)

con = MySQL(app)

registrar_blueprints(app)

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__ =="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)