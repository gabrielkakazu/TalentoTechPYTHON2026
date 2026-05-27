import sqlite3

# Conectamos con la base
conexion = sqlite3.connect("prueba123.db")
cursor = conexion.cursor()

# Datos a actualizar
id_producto = 2
nuevo_precio = 420.0

# Ejecutamos la actualización
cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id_producto))

# Guardamos y cerramos
conexion.commit()
conexion.close()

print(f"Producto con ID {id_producto} actualizado a ${nuevo_precio}.")

"""
📌 UPDATE tabla SET campo = valor WHERE condición modifica uno o más registros.

📌 Siempre usá WHERE para evitar modificar todos los registros por error.

🎯 Probá cambiar el ID o el precio para editar distintos productos.
"""
