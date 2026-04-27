pantalla = "Sistema de Gestión Básica de Productos \n 1. Agregar producto \n 2. Mostrar productos \n 3. Buscar producto \n 4. Eliminar producto \n 5. Salir"
print (pantalla)

productos = {}

while True:
    menu = input("Ingrese opción del 1 al 5 :")
    if not menu.isdigit() or int(menu) < 1 or int(menu) > 5:
        print("No ingresaste una opción válida! ")
        continue

    match int(menu):
        case 5:
            print("Gracias, vuelvas pronto")
            break
        case 2:
            print(f"Productos : {productos}")
        case 1:
            nombre = input("Ingrese nombre de producto: ").strip()

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
            print(f"Diccionario actual: {productos}")









