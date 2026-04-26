nombre = input("Decime tu nombre: ")
apellido = input("Decime tu apellido: ")
edad = input("Decime tu edad: ")
mail = input("Decime tu mail: ")
vacio = ""

nombreFormato = nombre.lower().capitalize()
apellidoFormato = apellido.lower().capitalize()

if nombre == vacio or apellido == vacio or int(edad) <= 18:
    print("ERROR!")
else:
    print(f"nombre: {nombreFormato} \n apellido: {apellidoFormato} \n edad: {edad} años \n mail: {mail}")
