from flask import Flask, Blueprint, redirect, url_for, request, render_template, session, jsonify
from bd import DatabaseController

registro = Blueprint('registro', __name__)

@registro.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        telefono = request.form['telefono']
        metodo_pago = request.form['metodo_pago']
        suscripcion = request.form['suscripcion']
        
        db = DatabaseController()
        db.connect()
        db.insert_data("usuarios", {
            "username": username,
            "password": password,
            "nombre": nombre,
            "apellidos": apellidos,
            "email": email,
            "telefono": telefono,
            "metodo_pago": metodo_pago,
            "suscripcion": suscripcion
        })
        db.close()
        
        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('registro.html')
