from flask import Blueprint

catalogo = Blueprint('catalogo', __name__)

@catalogo.route('/catalogo')
def otra_ruta():
    return 'ESTA SERÍA LA PÁGINA DEL CATALOGO!'
