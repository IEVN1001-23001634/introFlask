from flask import Blueprint, jsonify, request
from database import mysql

administrativos_bp = Blueprint(
    'administrativos',
    __name__,
    url_prefix='/api/administrativos'
)

def fila_a_diccionario(cursor, fila):
    columnas = [columna[0] for columna in cursor.description]
    return dict(zip(columnas, fila))

@administrativos_bp.route('', methods=['GET'])
def lista_administrativos():
    cursor = None

    try:
        cursor=mysql.connection.cursor()
        cursor.execute("""SELECT numempleado, nombre, apellidos, telefono, correo, departamento FROM administrativos""")
 
        datos=cursor.fetchall()
        administrativos=[
            fila_a_diccionario(cursor,fila)
            for fila in datos
        ]
 
        return jsonify({
            'administrativos': administrativos,
            'mensaje': 'Lista de administrativos',
            'exito': True
        }), 200

    except Exception:
        return jsonify({
            'mensaje': 'Error al consultar los administrativos',
            'exito': False
        }), 500

    finally:
        if cursor is not None:
            cursor.close()