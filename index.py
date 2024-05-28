from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory, session, jsonify
from carrito import carrito
from catalogo import catalogo
from registro import registro
from bd import DatabaseController

app = Flask(__name__)
app.register_blueprint(carrito)
app.register_blueprint(catalogo)
app.register_blueprint(registro)
app.secret_key = 'sie'  

@app.route('/')
def index():
    if 'username' in session:
        print(session['username'])
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':        
        bd = DatabaseController()
        bd.connect()
        print (bd.fetch_data("CLIENTE where email = '%s' and contraseña = '%s'" % (request.get_json().get('username'), request.get_json().get('password'))))
        if bd.fetch_data("CLIENTE where email = '%s' and contraseña = '%s'" % (request.get_json().get('username'), request.get_json().get('password'))):
            session['username'] = request.get_json().get('username')
            return jsonify({"message": "Login successful", "username": "ok"})
        else:
            print("Usuario o contraseña incorrectos")
    return send_from_directory('templates', 'login.html')

if __name__ == '__main__':
    app.run(debug=True)
