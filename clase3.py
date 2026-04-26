nombre = input("Decime tu nombre: ")
apellido = input("Decime tu apellido: ")
edad = input("Decime tu edad: ")
vacio = ""

if nombre == vacio or apellido == vacio or int(edad) <= 18:
    print("ERROR!")
else:
    print(f"{nombre} {apellido} tiene {edad} años")