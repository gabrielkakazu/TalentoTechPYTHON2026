# MENU DE OPCIONES
pantalla = "Sistema de Gestión Básica de Productos"
print (pantalla)

productos = {}

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
                
                    


        










