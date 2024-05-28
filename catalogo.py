from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory, session, jsonify

from bd import DatabaseController
catalogo = Blueprint('catalogo', __name__)

@catalogo.route('/catalogo')
def otra_ruta():
    if 'username' not in session:
        return redirect(url_for('login'))
    db = DatabaseController()
    db.connect()
    result = db.fetch_data("INVENTARIO where Stock > 0")
    db.close()
    print(result)
    return render_template('index.html', products=result)
    return str(result)

