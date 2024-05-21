from flask import Blueprint

registro = Blueprint('registro', __name__)

@registro.route('/registro')
def register():
    return 'ESTA SERÍA LA PÁGINA DEL REGISTRO!'
