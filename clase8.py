"""
* Crear un diccionario llamado productos donde las claves sean los nombres de los productos y los valores sean sus precios.
* Permitir que se agreguen productos y sus precios hasta que se decida finalizar.
* Mostrar el contenido del diccionario después de cada operación.
"""

productos = {}

while True:
    finalizar = input('Escriba "fin" para finalizar la carga de productos: ')
    if finalizar.lower().strip() == "fin":
        print("Gracias, vuelva pronto")
        break

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


"""
productos = {}

while True:
    finalizar = input("Escriba \"fin\" para finalizar la carga de productos ")
    if finalizar.lower().strip() == "fin":
        print("Gracias, vuelva pronto")
        break
    
    nombre = input("Ingrese nombre de producto: ")
    precio = input("Ingrese precio de producto: ")

    while nombre == "":
        print("[ALERTA] ¡El producto no puede tener un nombre vacío!")
        nombre = input("Vuelva a ingresar nombre: ")

    while not precio.isdigit():
        print("[ALERTA] ¡El precio tiene ser en números!")
        precio = input("Vuelva a ingresar precio :")
        if precio.isdigit() and float(precio) <= 0:
            print("[ALERTA] ¡El precio tiene ser en números!")
            precio = input("Vuelva a ingresar precio :")

    productos.setdefault(nombre, float(precio))
    print(f"Este es el diccionario con {productos}")
"""

