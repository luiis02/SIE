import sqlite3

class DatabaseController:
    def __init__(self):
        self.db_name = "bd.sqlite"
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print("Conexión establecida con la base de datos")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def create_table(self, table_name, columns):
        try:
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print(f"Tabla {table_name} creada correctamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla {table_name}: {e}")
    
    def insert_data(self, table_name, data):
        try:
            placeholders = ', '.join(['?' for _ in range(len(data))])
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(insert_query, data)
            self.connection.commit()
            print("Datos insertados correctamente")
        except sqlite3.Error as e:
            print(f"Error al insertar datos en la tabla {table_name}: {e}")
    
    def fetch_data(self, table_name):
        try:
            select_query = f"SELECT * FROM {table_name}"
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error al obtener datos de la tabla {table_name}: {e}")
            return None
    
    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada correctamente")