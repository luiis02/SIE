from flask import Blueprint, render_template, request, redirect, url_for

atencion_cliente = Blueprint('atencion_cliente', __name__)

@atencion_cliente.route('/atencion_cliente')
def atencion_cliente_page():
    return render_template('atencion_cliente.html')

@atencion_cliente.route('/enviar_consulta', methods=['POST'])
def enviar_consulta():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    # Aquí puedes procesar y almacenar los datos si es necesario

    # Construir la URL de WhatsApp
    whatsapp_url = f"https://wa.link/5drjts?text={nombre}%20{email}%20{mensaje}"
    return redirect(whatsapp_url)
