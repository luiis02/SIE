import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('bd.sqlite')

# Crear un cursor
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS INVENTARIO (
    Codigo_producto INTEGER PRIMARY KEY,
    Nombre TEXT(32),
    Stock INTEGER(4),
    Puntuación INTEGER(2),
    Añada INTEGER(4),
    Precio_producto INTEGER(3),
    Pasillo_almacen INTEGER(2),
    Codigo_almacen INTEGER(5),
    Codigo_botella INTEGER(3),
    Codigo_uva INTEGER(3),
    Codigo_caja INTEGER(3)
)
''')

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()
