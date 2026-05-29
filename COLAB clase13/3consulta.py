import sqlite3

# Conectamos con la base
conexion = sqlite3.connect("prueba123.db")
cursor = conexion.cursor()

# cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", 
# ("MERCA", 999999.0))

# Ejecutamos la consulta
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

# Cerramos la conexión
conexion.close()

# Mostramos los resultados
print("Lista de productos:")
for producto in productos:
    id_, nombre, precio = producto
    print(f"{id_}. {nombre} - ${precio}")

"""
📌 SELECT * trae todos los campos de todos los registros.

📌 fetchall() guarda los resultados en una lista de tuplas.

📌 Cada tupla contiene: (id, nombre, precio).

🎯 Probá ejecutar este bloque después de insertar productos nuevos.
"""
