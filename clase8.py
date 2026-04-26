"""
* Crear un diccionario llamado productos donde las claves 
sean los nombres de los productos y los valores sean sus precios.
* Permitir que se agreguen productos y sus precios hasta que se decida finalizar.
* Mostrar el contenido del diccionario después de cada operación.
"""

productos = {}

while True:
    finalizar = input("Escriba \"fin\" para finalizar la carga")
    if finalizar.lower().strip() == "fin":
        print("Gracias, vuelva pronto")
        break
    else:
        print(productos)
        # acá falta todo

