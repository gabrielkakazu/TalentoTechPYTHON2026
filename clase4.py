nombre = input("Decime tu nombre: ")
apellido = input("Decime tu apellido: ")
edad = int(input("Decime tu edad: "))
mail = input("Decime tu mail: ")
vacio = ""


nombreFormato = nombre.lower().capitalize()
apellidoFormato = apellido.lower().capitalize()
mailCorrecto = " " not in mail and mail.count("@") == 1 

if nombre == vacio or apellido == vacio or not mailCorrecto:
    print("ERROR!")
else:
    print(f" nombre: {nombreFormato} \n apellido: {apellidoFormato} \n edad: {edad} años \n mail: {mail}")

if edad < 15:
    print("Niño/a")
elif edad <=18:
    print("Adolescente")
else:
    print("Adulto/a")
