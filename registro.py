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
        print(username)
        print(password)
        db = DatabaseController()
        db.connect()
        todos = db.fetch_data("CLIENTE")
        cod = len(todos)+1
        print(cod)
        db.insert_data("CLIENTE", [
             cod,
             username,
            password,
             nombre,
             apellidos,
             email,
             telefono,
             metodo_pago,
             suscripcion
        ])
        db.close()
        
        session['username'] = username
        return redirect(url_for('index'))
    
    return render_template('registro.html')
