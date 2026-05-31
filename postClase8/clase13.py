import sqlite3

def crearDB():
    conexion = sqlite3.connect("alumnos2.db")
    print("Conexión establecida exitosamente.")
    conexion.close()

def crearTabla():
    conexion = sqlite3.connect("alumnos2.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parcial1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        apellido TEXT NOT NULL,
        nota FLOAT NOT NULL)
        ''')
    conexion.commit()
    print("Tabla parcial1 creada exitosamente")
    conexion.close()

if __name__ == "__main__":
    # crearDB()
    # crearTabla()
    pass

