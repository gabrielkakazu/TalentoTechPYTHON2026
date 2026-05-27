import sqlite3

# Conectamos con la base
conexion = sqlite3.connect("prueba123.db")
cursor = conexion.cursor()

# Creamos la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
""")

# Cerramos la conexión
conexion.commit()
conexion.close()

print("Tabla 'productos' creada correctamente.")

"""
📌 cursor.execute(...) permite enviar una instrucción SQL desde Python.

📌 Usamos CREATE TABLE IF NOT EXISTS para evitar errores si la tabla ya existe.

📌 id será el número autogenerado que identifica a cada producto.

🎯 Probá ejecutar este bloque más de una vez: no se va a duplicar la tabla.
"""
