# MENU DE OPCIONES
pantalla = "Sistema de Gestión Básica de Productos"
print (pantalla)

def menu():
    """ Muestra en pantalla las opciones del Sistema de Gestion:
    1. Ingresar productos
    2. Mostrar productos
    3. Buscar productos
    4. Eliminar productos
    5. Salir
    """
    print(" 1. Ingresar productos\n 2. Mostrar productos\n 3. Buscar producto\n 4. Eliminar producto\n 5. Salir\n")

def separador() :
    # Un separador para aplicar a cada interracción con el mení
    print("---")

productos = {}

def agregar_producto():
    """
    Solicita por consola un nombre de producto (str) y un precio (int).
    El bucle while se rompe:
     - al ingresar un nombre vacío
     - si precio es menor o igual a 0
     - si el nombre y el precio son válidos,después de agregarlo al diccionario productos

    """
    while True:
        nombre = input("Ingrese nombre de producto: ").strip()
        precio = int(input("Ingrese un precio al producto (mayor a 0): "))
        nombreFormateado = nombre.lower()
        # precioAIngresar = int(input("Ingrese precio para el producto: "))
        if not nombre or not precio or nombreFormateado in productos:
            print("Lo siento, precio y nombre no pueden ser vacíos!\nNi tampoco puede ser un nombre repetido")
            break
        elif isinstance(precio, int) and precio > 0:
            productos[nombreFormateado] = precio
            print(f"Producto {nombreFormateado} agregado con éxito!\nSale ${precio}")
            separador()
            break
        else: 
            print("Lo siento, precio no es válido!")
            break
    separador()

def consultar_productos():
    if productos:
        print("Lista de productos:")
        for i, nombre in enumerate(productos, start=1):
            print(f"{i}. {nombre.capitalize()} sale ${productos[nombre]}")
    else:
        print("Lista de productos vacía.")
    separador()    

def buscar_producto():
    """
    """
    while True:
        productoBuscado = input("Ingrese nombre de producto: ").strip().lower()
        if productoBuscado not in productos:
            print("Lo siento, el producto no esta disponible... ")
                    
        else:
            print(f"Aquí tenemos {productoBuscado} a un precio de ${productos.get(productoBuscado)}")
                
            salir = input("Presione 's' para volver a Menu Inicial ")
            if salir.lower().strip() == "s":
                print("Volviendo a Menú Inicial...")
                break

def borrar_producto():
    while True:
        productoABorrar = input("Ingrese nombre de producto a eliminar: ")
        if productoABorrar.lower().strip() not in productos:
            print("Lo siento, el producto no existe en nuestra BD")
            break
        else:
            print(f"Eliminamos {productoABorrar} de nuestra BD")
            del productos[productoABorrar]
            break
    separador()

            

    """if productos:
        productoABorrar = input("Ingrese nombre de producto a borrar: ")
        if productoABorrar in productos:
            productos.pop(productoABorrar)
            print(f"Se eliminó {productoABorrar} de la lista.")
            separador()
        else:
            print(f"No se encuentra en la lista {productoABorrar}")
            separador()"""

def mostrar_menu():
    while True:
        menu()
        opcion = input("Ingresa una opcion (1-5): ")

        match opcion.strip():
            case "1":
                agregar_producto()
            case "2":
                consultar_productos()
            case "3":
                print("buscando producto... función incompleta") #TODO
            case "4":
                borrar_producto()
            case "5":
                print("Gracias, vuelvas pronto")
                print("Gestion de productos desarrollado por @GabrielKakazu")
                print("Talento Tech 2026 - Iniciación a Python")
                break
            case _:
                print("Lo siento, no ingresó una opción válida")

mostrar_menu()
        



"""
while True:
    
    menu = input(" 1. Ingresar productos\n 2. Mostrar productos\n 3. Buscar producto\n 4. Eliminar producto\n 5. Salir\nIngrese opción del 1 al 5 :")
    # VALIDACION DE OPCIONES
    if not menu.isdigit() or int(menu) < 1 or int(menu) > 5:
        print("No ingresaste una opción válida! ")
        continue

    match int(menu):
        # OPCION SALIDA DE MENU
        case 5:
            print("Gracias, vuelvas pronto")
            print("Gestion de productos desarrollado por @GabrielKakazu")
            print("Talento Tech 2026 - Iniciación a Python")
            break

        # OPCION MOSTRAR PRODUCTOS
        case 2:
            print("Tenemos los siguientes productos: ")
            contador = 1
            for nombre in productos:
                print(f"Prod nro {contador}: {nombre} a un precio de ${productos[nombre]}")
                contador += 1
            print("Volviendo a Menú Inicial...")

        # OPCION INGRESAR PRODUCTOS
        case 1:
            while True:
                nombre = input("Ingrese nombre de producto: ").strip()
                
                # VALIDACION DE NOMBRE DE PRODUCTO NO VACÍO 
                while nombre == "":
                    print("[ALERTA] ¡El producto no puede tener un nombre vacío!")
                    nombre = input("Vuelva a ingresar nombre: ").strip()

                # Validación de precio
                while True:
                    precio = input("Ingrese precio de producto: ")
                    try:
                        precio = float(precio)
                        if precio <= 0:
                            print("[ALERTA] ¡El precio debe ser mayor que 0!")
                        else:
                            break
                    except ValueError:
                        print("[ALERTA] ¡El precio debe ser un número válido!")

                productos[nombre] = precio
                print(f"Productos actuales: {productos}")

                salir = input("Ingrese cualquier tecla ó 's' para volver a Menu Inicial ")
                if salir.lower().strip() == "s":
                    print("Volviendo a Menú Inicial...")
                    break   

        # BUSQUEDA DE PRODUCTOS
        case 3:
            while True:
                productoBuscado = input("Ingrese nombre de producto: ")
                if productoBuscado not in productos:
                    print("Lo siento, el producto no esta disponible... ")
                    
                else:
                    print(f"Aquí tenemos {productoBuscado} a un precio de ${productos.get(productoBuscado)}")
                
                salir = input("Presione 's' para volver a Menu Inicial ")
                if salir.lower().strip() == "s":
                    print("Volviendo a Menú Inicial...")
                    break
        
        # ELIMINAR PRODUCTOS
        case 4:
                     
            while True:
                productoABorrar = input("Ingrese nombre de producto a eliminar: ")
                if productoABorrar.lower().strip() not in productos:
                        print("Lo siento, el producto no existe en nuestra BD")
                else:
                    print(f"Eliminamos {productoABorrar} de nuestra BD")
                    del productos[productoABorrar]

                salir = input("Presione S para volver al Menu Inicial :")
                if salir.lower().strip() == "s":
                    print("Volviendo a Menú Inicial")
                    break
"""