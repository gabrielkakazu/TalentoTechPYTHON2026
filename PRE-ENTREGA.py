# MENU DE OPCIONES
pantalla = "Sistema de Gestión Básica de Productos"
print (pantalla)

productos = []

while True:
    
    menu = input(" 1. Ingresar productos\n 2. Mostrar productos\n 3. Buscar producto\n 4. Eliminar producto\n 5. Salir\nIngrese opción del 1 al 5 :")
    # VALIDACION DE OPCIONES
        
    match menu:
        # OPCION SALIDA DE MENU
        case "5":
            print("Gracias, vuelvas pronto")
            print("Gestion de productos desarrollado por @GabrielKakazu")
            print("Talento Tech 2026 - Iniciación a Python")
            break

        # OPCION MOSTRAR PRODUCTOS
        case "2":
            if productos == []:
                print("No tenemos productos disponibles")
                continue

            print("Tenemos los siguientes productos: ")
            contador = 1
            for producto in productos:
                nombre = producto[0]
                precio = producto[1]
                categoria = producto[2]
                print(f"Prod nro {contador}: {nombre} de la categoria {categoria} a un precio de ${precio}")
                contador += 1
            print("Volviendo a Menú Inicial...")

        # OPCION INGRESAR PRODUCTOS
        case "1":
            while True:
                nuevoProducto = []
                
                while True:
                    nombre = input("Ingrese nombre de producto: ").strip()
                    
                
                    # VALIDACION DE NOMBRE DE PRODUCTO NO VACÍO 
                    while nombre == "":
                        print("[ALERTA] ¡El producto no puede tener un nombre vacío!")
                        nombre = input("Vuelva a ingresar nombre: ").strip()
                    
                    nuevoProducto.append(nombre.lower())
                        
                    precio = input("Ingrese precio de producto: ")
                    try:
                        precio = float(precio)
                        if precio <= 0:
                            print("[ALERTA] ¡El precio debe ser mayor que 0!")
                        else:
                            nuevoProducto.append(precio)
                            
                            
                    except ValueError:
                        print("[ALERTA] ¡El precio debe ser un número válido!")
                        break
                    
                    categoria = input("Ingrese categoria de producto: ").strip()
                    while categoria == "":
                        print("[ALERTA] ¡La categoria no puede ser vacía!")          
                    
                    nuevoProducto.append(categoria.upper())
                    productos.append(nuevoProducto)
                    break
                
                print(f"Productos actuales: {productos}")

                salir = input("Ingrese cualquier tecla ó la tecla 'v' para volver al Menu Inicial ")
                if salir.lower().strip() == "v":
                    print("Volviendo a Menú Inicial...")
                    break   

        # BUSQUEDA DE PRODUCTOS
        case "3":
            while True:
                productoBuscado = input("Ingrese nombre de producto: ").strip().lower()
                for producto in productos:
                    if productoBuscado == producto[0]:
                        nombre = producto[0]
                        precio = producto[1]
                        categoria = producto[2]
                        print(f"Tenemos {nombre} de la categoria {categoria} a un precio de ${precio}")      
                        break
                else:
                    print(f"Lo siento no tenemos {productoBuscado}")
                                       
                salir = input("Presione 'v' para volver a Menu Inicial ")
                if salir.lower().strip() == "v":
                    print("Volviendo a Menú Inicial...")
                    break
                
        
        # ELIMINAR PRODUCTOS
        case "4":
            while True:
                productoBuscado = input("Ingrese nombre de producto para eliminar: ").strip().lower()
                for producto in productos:
                    if productoBuscado == producto[0]:
                        productos.remove(producto)       
                        print(f"Se ha eliminado {productoBuscado} de la lista de productos.")                
                        break

                else:
                    print(f"Lo siento no tenemos {productoBuscado} en la lista")
                                       
                salir = input("Presione 'v' para volver a Menu Inicial ")
                if salir.lower().strip() == "v":
                    print("Volviendo a Menú Inicial...")
                    break                     


        case _:
            print("No ingresaste una opción válida! ")
            continue
