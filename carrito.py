from flask import Blueprint

carrito = Blueprint('carrito', __name__)

@carrito.route('/carrito')
def otra_ruta():
    return 'ESTA SERÍA LA PÁGINA DEL CARRITO!'
