"""
* Crear un diccionario llamado productos donde las claves sean los nombres de los productos y los valores sean sus precios.
* Permitir que se agreguen productos y sus precios hasta que se decida finalizar.
* Mostrar el contenido del diccionario después de cada operación.
"""

productos = {}

while True:
    finalizar = input("Escriba \"fin\" para finalizar la carga de productos ")
    if finalizar.lower().strip() == "fin":
        print("Gracias, vuelva pronto")
        break
    
    nombre = input("Ingrese nombre de producto: ")
    precio = int(input("Ingrese precio de producto: "))

    while nombre == "":
        print("[ALERTA] ¡El producto no puede tener un nombre vacío!")
        nombre = input("Vuelva a ingresar nombre: ")

    while precio <= 0:
        print("[ALERTA] ¡El precio no puede ser 0 o negativo!")
        precio = int(input("Vuelva a ingresar precio :"))
        

    productos.setdefault(nombre, precio)
    print(f"Este es el diccionario con {productos}")


