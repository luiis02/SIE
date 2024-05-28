from flask import Blueprint
from bd import DatabaseController
catalogo = Blueprint('catalogo', __name__)

@catalogo.route('/catalogo')
def otra_ruta():
    db = DatabaseController()
    db.connect()
    result = db.fetch_data("INVENTARIO")
    db.close()
    return str(result)
