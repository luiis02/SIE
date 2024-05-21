from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory
from carrito import carrito
from catalogo import catalogo


app = Flask(__name__)
app.register_blueprint(carrito)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #####AQUI SOLO QUEDARIA LLAMAR A LA BD Y COMPROBAR QUE EL USUARIO EXISTE
        if request.form['username'] == 'luis' and request.form['password'] == '123':
            print('Intentando acceder')
            return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)
