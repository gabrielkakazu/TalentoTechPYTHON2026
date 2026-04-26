# BUCLE while
ingresos = []
mesActual = 1

while len(ingresos) < 6:
    nuevoIngreso = float(input(f"Inserte ingresos en nros del mes {mesActual} : "))
    if (nuevoIngreso >= 0):
        ingresos.append(nuevoIngreso)
        mesActual += 1
    else:
        print("Perdón, pero el ingreso no puede ser menor a 0")

totalIngresos =  sum(ingresos)
promedioIngresos = totalIngresos / len(ingresos)
print("Esta es la lista de ingresos mensuales")
print(ingresos)
print(f"Total de ingresos: {totalIngresos}")
print(f"Promedio de ingresos mensuales: {promedioIngresos}")
