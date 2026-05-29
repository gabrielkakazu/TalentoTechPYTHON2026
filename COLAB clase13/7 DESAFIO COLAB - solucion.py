import sqlite3

def conectar():
    return sqlite3.connect("productos.db")

def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    try:
        precio = float(input("Precio del producto: "))
        with conectar() as con:
            con.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        print("Producto agregado correctamente.")
    except ValueError:
        print("Precio inválido.")

def listar_productos():
    with conectar() as con:
        cursor = con.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if productos:
            print("\n Lista de productos:")
            for id_, nombre, precio in productos:
                print(f"{id_}. {nombre} - ${precio}")
        else:
            print("No hay productos registrados.")

def modificar_precio():
    try:
        id_producto = int(input("ID del producto a modificar: "))
        nuevo_precio = float(input("Nuevo precio: "))
        with conectar() as con:
            con.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id_producto))
        print("Precio actualizado.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_producto():
    try:
        id_producto = int(input("ID del producto a eliminar: "))
        with conectar() as con:
            con.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        print("Producto eliminado.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Modificar precio")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            modificar_precio()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida.")

# Ejecutamos el menú
menu()
