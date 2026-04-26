# bucle FOR y RANGE()
clientes = []

while len(clientes) < 6:
    nuevoCliente = input("Inserte nuevo cliente : ")
    nuevoClienteFormato = nuevoCliente.lower().capitalize()
    if (nuevoClienteFormato not in clientes):
        clientes.append(nuevoClienteFormato)        
    else:
        print("Perdón, pero ese cliente ya estaba en la lista")

print(clientes)

for cliente in clientes:
    posicion = clientes.index(cliente)
    if cliente =="":
        print(f"Cliente {posicion}: [ALERTA] Nombre no válido")    
    else: 
        print(f"Cliente {posicion}: {cliente}")

