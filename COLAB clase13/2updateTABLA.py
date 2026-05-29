import sqlite3

# Conectamos con la base
conexion = sqlite3.connect("prueba123.db")
cursor = conexion.cursor()

# Insertamos algunos productos
cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Pan", 250.0))
cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Leche", 390.0))
cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Café", 1200.0))

# Guardamos y cerramos
conexion.commit()
conexion.close()

print("Productos agregados correctamente.")

"""
📌 Usamos ? como marcadores de posición, y pasamos los valores aparte como una tupla.

📌 Esto ayuda a evitar errores y protege contra posibles ataques de inyección de SQL.

🎯 Probá agregar más productos o modificar los valores. Más adelante vamos a ver cómo cargar productos usando input().
"""

