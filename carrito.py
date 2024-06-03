from flask import Flask, Blueprint, redirect, url_for, request, render_template, send_file, send_from_directory, session, jsonify
from bd import DatabaseController
import random   
carrito = Blueprint('carrito', __name__)

@carrito.route('/carrito')
def otra_ruta2():
    if 'username' not in session:
        return redirect(url_for('login'))
    bd = DatabaseController()
    bd.connect()
    user_id = bd.fetch_data('CLIENTE where Email = "%s"' % session['username'],)[0][0]
    carrito = bd.fetch_data('CARRITO where CodCliente = "%s"' % user_id)
    print(carrito)
    productos = []
    for prod in carrito:
        producto = bd.fetch_data('INVENTARIO WHERE Codigo_producto = %s' % prod[1])
        print(producto)
        if producto:
            productos.append(producto[0])   

    bd.close()
    return render_template('carrito.html', carrito=carrito, productos=productos)
@carrito.route('/add_carrito', methods=['POST'])
def add_carrito():
    product_id = request.form['product_id']
    bd = DatabaseController()
    bd.connect()
    print(bd.fetch_data('CLIENTE where Email = "%s"' % session['username'],))
    user_id = bd.fetch_data('CLIENTE where Email = "%s"' % session['username'],)[0][0]
    print(bd.fetch_data('INVENTARIO where Codigo_producto = "%s"' % product_id,))
    precio_prod = bd.fetch_data('INVENTARIO where Codigo_producto = "%s"' % product_id,)[0][5]
    bd.insert_data('CARRITO', [user_id, product_id,1,0,precio_prod])
    print(user_id)  
    bd.close()
    print(f"Usuario: {session['username']}")
    print(f"Producto añadido al carrito: {product_id}")
    return redirect('/catalogo')


@carrito.route('/update-product-quantity', methods=['POST'])
def update_product_quantity():
    data = request.get_json()
    product_id = data['productId']
    cantidad = data['cantidad']
    bd = DatabaseController()
    bd.connect()
    user_id = bd.fetch_data('CLIENTE where Email = "%s"' % session['username'],)[0][0]
    if cantidad < 1:
        bd.cursor.execute(f"DELETE FROM CARRITO WHERE CodCliente = {user_id} AND CodProd = {product_id}")
    else:
        bd.cursor.execute(f"UPDATE CARRITO SET Cantidad = {cantidad} WHERE CodCliente = {user_id} AND CodProd = {product_id}")
    bd.connection.commit()
    bd.close()
    response = {
        'productId': product_id,
        'cantidad': cantidad,
        'status': 'success'
    }
    redirect('/catalogo')

@carrito.route('/finalizar_compra', methods=['POST'])
def finalizar_compra():
    bd = DatabaseController()
    bd.connect()
    user_id = bd.fetch_data('CLIENTE where Email = "%s"' % session['username'],)[0][0]
    try:
        n_factura = bd.fetch_data('FACTURAS',)[0][0] + 1
        n_factura = len(n_factura)+1
    except:
        n_factura = random.randint(1, 1000000000000)
    carrito = bd.fetch_data('CARRITO where CodCliente = "%s"' % user_id)
    print(carrito)
    print(user_id)
    bd.insert_data('FACTURAS', [n_factura, '00/00/00' , '21', user_id, 'FF00DWS'])
    for prod in carrito:
        bd.insert_data('PEDIDOS', [n_factura, prod[1], user_id, prod[4] * prod[2], '', 'Iniciado', ''])
        bd.cursor.execute(f"DELETE FROM CARRITO WHERE CodCliente = {user_id}")
    bd.connection.commit()
    bd.close()
    return jsonify({'status': 'success'})