# CLASE 7 Listas y Tuplas

# bucle FOR y RANGE()
clientes = []

finalizar = ""
while True:
    nuevoCliente = input("Inserte nuevo cliente o escriba \"fin\" para finalizar.")
    if nuevoCliente.lower().strip() == "fin":
        break
    else:
        nuevoClienteFormato = nuevoCliente.lower().capitalize()    
        if (nuevoCliente == ""):
            print("[ALERTA!] El nuevo cliente no puede ser vacio")
        elif nuevoClienteFormato in clientes:
            print("Perdón, ese cliente ya existe en nuestra lista")
        else:
            clientes.append(nuevoClienteFormato)        
            

print(clientes)

# sorted(lista) crea una nueva lista con los elementos ordenados

clientesOrdenados = sorted(clientes)
for cliente in clientesOrdenados:
    posicion = clientesOrdenados.index(cliente)
    if cliente =="":
        print(f"Cliente {posicion}: [ALERTA] Nombre no válido")    
    else: 
        print(f"Cliente {posicion}: {cliente}")