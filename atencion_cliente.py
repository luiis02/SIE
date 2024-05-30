from flask import Blueprint, render_template

atencion_cliente = Blueprint('atencion_cliente', __name__)

@atencion_cliente.route('/atencion_cliente')
def atencion_cliente_page():
    return render_template('atencion_cliente.html')
