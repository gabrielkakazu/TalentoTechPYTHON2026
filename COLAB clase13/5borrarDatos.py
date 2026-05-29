import sqlite3

# Conectamos con la base
conexion = sqlite3.connect("prueba123.db")
cursor = conexion.cursor()

# ID del producto a eliminar
id_a_borrar = 1

# Ejecutamos la eliminación
cursor.execute("DELETE FROM productos WHERE id = ?", (id_a_borrar,))
# cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("MERCA", 999999.0))

# Guardamos y cerramos
conexion.commit()
conexion.close()

print(f"Producto con ID {id_a_borrar} eliminado.")

"""
¿Qué hace este código?

📌 DELETE FROM tabla WHERE condición elimina uno o más registros.

⚠️ Si olvidás el WHERE, se borran todos los productos.

🎯 Probá eliminar productos distintos y luego consultá la lista con SELECT para ver los cambios.
"""
