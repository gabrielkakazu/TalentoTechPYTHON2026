"""
# Lista de tareas
tareas = ["barrer", "lavar los platos", "hacer la cama"]

# Abrimos el archivo en modo escritura
with open("tareas.txt", "w") as archivo:
    for tarea in tareas:
        archivo.write(tarea + "\n")

print("Tareas guardadas en el archivo.") 
"""

"""
📌 with open("tareas.txt", "w") abre (y si no existe, crea) un archivo de texto para escritura.

📌 .write() escribe cada línea. Agregamos \n para que cada tarea vaya en una línea nueva.

📌 El bloque with se encarga de cerrar el archivo automáticamente.

"""

# Abrimos el archivo en modo lectura
"""with open("tareas.txt", "r") as archivo:
    print("📄 Tareas registradas:")
    for linea in archivo:
        print("-", linea.strip())"""

"""
📌 open("tareas.txt", "r") abre el archivo en modo lectura.

📌 El bucle for recorre cada línea del archivo.

📌 .strip() elimina el salto de línea (\n) que se guardó al escribir.

🎯 Probá modificar el archivo manualmente y luego volver a leerlo desde el código.
"""


"""
Cuando algo puede fallar (por ejemplo, una división, una conversión o un acceso a archivo),
usamos try-except para evitar que el programa se corte.

En este ejemplo, intentamos convertir una entrada en número.
"""
entrada = input("Ingresá un número: ")
"""
try:
    numero = int(entrada)
    print("El doble es:", numero * 2)
except:
    print("Eso no era un número válido.")
"""

# Escribe aqui tu programa
with open("notas.txt", "w") as archivoEscribir:
  while True:
    entrada = input("Ingrese un nro entre 1 y 10 o 'salir' para salir.")
    if entrada.lower().strip() == "salir":
      print("Gracias por ingresar notas.")
      break
    try:
      entradaEnRango = int(entrada)
      if entradaEnRango > 0 and entradaEnRango <= 10:
        archivoEscribir.write(f"* {entradaEnRango}\n")
      else:
        print("La nota está fuera del rango.")
    except:
      print("No ingresaste un nro válido")


with open("notas.txt", "r") as archivoLectura:
    print("Notas registradas:")
    for linea in archivoLectura:
        print("Nota obtenida:" + linea.strip())