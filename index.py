from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory, session
from carrito import carrito
from catalogo import catalogo
from bd import DatabaseController

app = Flask(__name__)
app.register_blueprint(carrito)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        bd = DatabaseController()
        bd.connect()
        if bd.fetch_data("usuarios where email = '%s' and password = '%s'" % (request.form['username'], request.form['password'])):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return send_from_directory('static', 'index.html')



if __name__ == '__main__':
    app.run(debug=True)
