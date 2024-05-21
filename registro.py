from flask import Blueprint

registro = Blueprint('registro', __name__)

@registro.route('/registro')
def otra_ruta():
    return 'ESTA SERÍA LA PÁGINA DEL REGISTRO!'
