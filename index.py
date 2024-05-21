from flask import Flask, Blueprint
from carrito import carrito
from catalogo import catalogo


app = Flask(__name__)
app.register_blueprint(carrito)

@app.route('/')
def hello_world():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)
