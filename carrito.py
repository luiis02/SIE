from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory, session, jsonify

carrito = Blueprint('carrito', __name__)

@carrito.route('/carrito')
def otra_ruta2():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('carrito.html')