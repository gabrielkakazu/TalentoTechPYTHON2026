import sqlite3

def conectarBD(nombre):
    conexion = sqlite3.connect(nombre + ".db")
    print(f"La base de datos {nombre} ha sido abierta (o creada) correctamente")
    return conexion

def crearTablaEnBD(nombre_bd):
    with sqlite3.connect(nombre_bd + ".db") as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
        """)

        conexion.commit()

    print("Tabla creada correctamente.")

def insertarRegistros(nombre_bd):
        with sqlite3.connect(nombre_bd + ".db") as conexion:
            cursor = conexion.cursor()

            nombreAInsertar = input("Escriba nombre de producto: ")
            precioAInsertar = float(input("Escriba precio: "))

            cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombreAInsertar, precioAInsertar))

            conexion.commit()

            print("Producto agregado correctamente.")

def consultar(nombre_db):
    conexion = conectarBD(nombre_db)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()

    # Mostramos los resultados
    print("Lista de productos:")
    for producto in productos:
        id_, nombre, precio = producto
        print(f"{id_}. {nombre} - ${precio}")

def actualizarNombre(nombre_db):
    conexion = conectarBD(nombre_db)
    cursor = conexion.cursor()

    nuevoNombre = input("Ingrese nuevo nombre: ")

    registroID = int(input("Ingrese ID de producto "))

    cursor.execute(
        "UPDATE productos SET nombre = ? WHERE id = ?", 
        (nuevoNombre, registroID)
    )

    conexion.commit()
    conexion.close()

    print(f"Producto con ID {str(registroID)} actualizado a {nuevoNombre}.")

def actualizarPrecio(nombre_db):
    conexion = conectarBD(nombre_db)
    cursor = conexion.cursor()

    registroID = int(input("Ingrese ID de producto "))

    nuevoPrecio = float(input("Ingrese nuevo precio: "))

    cursor.execute(
        "UPDATE productos SET precio = ? WHERE id = ?", 
        (nuevoPrecio, registroID)
    )

    conexion.commit()
    conexion.close()

    print(f"Producto con ID {str(registroID)} actualizado a ${nuevoPrecio}.")

def borrarRegistro(nombre_bd):
    conexion = conectarBD(nombre_bd)
    cursor = conexion.cursor()

    id_a_borrar = int(input("Ingrese ID de producto a borrar "))

    cursor.execute(
        "DELETE FROM productos WHERE id = ?", 
        (id_a_borrar,)
    )

    conexion.commit()
    conexion.close()

    print(f"Producto con ID {id_a_borrar} eliminado.")
    print("La nueva lista es...")
    consultar("productos")








if __name__ == "__main__":
    # conectarBD("productos")
    # crearTablaEnBD("productos")
    # insertarRegistros("productos")
    consultar("productos")
    # actualizarPrecio("productos")
    borrarRegistro("productos")
    











"""
Desafío - Registro de notas con validación

Vas crear un pequeño sistema para gestionar productos, pero esta vez usando una base de datos real con SQLite.

🔧 ¿Qué tiene que hacer tu programa?

    Mostrar un menú con 4 opciones:
        Agregar un nuevo producto
        Listar todos los productos
        Cambiar el precio de un producto
        Eliminar un producto

    Usar input() para pedir los datos al usuario (nombre, precio, id, etc.)

    Validar los valores ingresados (por ejemplo, que el precio sea un número válido)

    Mostrar mensajes claros de éxito o error en cada operación

💡 Algunas sugerencias:

    Usá INSERT, SELECT, UPDATE y DELETE desde Python con sqlite3
    Usá try-except si querés prevenir errores inesperados
    Probá ejecutar varias operaciones seguidas y consultá al final para ver los resultados

🎯 Este ejercicio resume todos los conceptos trabajados en esta clase. ¡A ponerlo en práctica!

(Intenta resolverlo antes de mirar la posible solución que aparece más abajo!)
"""