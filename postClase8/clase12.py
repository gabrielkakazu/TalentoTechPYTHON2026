nombre = input("ingrese nombre :")
apellido = input ("ingrese apellido :")
correo = input("ingrese mail :")

try:
    archivo = open("clientes.txt", "w")
    archivo.write(f"Nombre: {nombre.lower().capitalize()}\n")
    archivo.write(f"Apellido: {apellido.lower().capitalize()}\n" )
    if correo.count("@") == 1 and " " not in correo.strip():
        archivo.write(f"correo: {correo}" + "\n")
    else:
        print("Correo incorrecto.")
        archivo.write("correo: sin mail\n")
    archivo.close()
except:
    print("[ERROR] No se puedo guardar la información.")


try:
    archivo = open("clientes.txt", "r")
    print("=== Registro de Clientes ===")
    for linea in archivo.readlines():
        print(linea)
    archivo.close()
except:
    print("[ERROR] archivo no se puede leer.")

        



