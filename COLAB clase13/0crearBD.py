import sqlite3

# Nos conectamos (o creamos el archivo si no existe)
conexion = sqlite3.connect("prueba123.db")

# Cerramos la conexión por ahora
conexion.close()

print("Base de datos creada (o abierta) correctamente.")
