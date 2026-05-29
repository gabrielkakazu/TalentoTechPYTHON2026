import sqlite3

# Función para conectar
def conectar():
    return sqlite3.connect("alumnos.db")

# Agregar un nuevo alumno
def agregar_alumno():
    nombre = input("Nombre: ").strip()
    try:
        edad = int(input("Edad: "))
        email = input("Correo electrónico: ").strip()

        with conectar() as con:
            con.execute("INSERT INTO alumnos (nombre, edad, email) VALUES (?, ?, ?)", (nombre, edad, email))
        print("Alumno agregado.")
    except ValueError:
        print("Edad inválida.")

# Listar todos los alumnos
def listar_alumnos():
    with conectar() as con:
        cursor = con.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()
        if alumnos:
            print("\nAlumnos registrados:")
            for id_, nombre, edad, email in alumnos:
                print(f"{id_}. {nombre} ({edad} años) – {email}")
        else:
            print("No hay alumnos registrados.")

# Modificar email
def modificar_email():
    try:
        id_alumno = int(input("ID del alumno: "))
        nuevo_email = input("Nuevo email: ").strip()
        with conectar() as con:
            cursor = con.execute("UPDATE alumnos SET email = ? WHERE id = ?", (nuevo_email, id_alumno))
            if cursor.rowcount > 0:
                print("Email actualizado.")
            else:
                print("No se encontró ese ID.")
    except ValueError:
        print("ID inválido.")

# Eliminar un alumno con confirmación
def eliminar_alumno():
    try:
        id_alumno = int(input("ID del alumno a eliminar: "))
        confirmar = input(f"¿Eliminar al alumno con ID {id_alumno}? (s/n): ").strip().lower()
        if confirmar == "s":
            with conectar() as con:
                cursor = con.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
                if cursor.rowcount > 0:
                    print("Alumno eliminado.")
                else:
                    print("No se encontró ese ID.")
        else:
            print("Operación cancelada.")
    except ValueError:
        print("ID inválido.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar alumno")
        print("2. Listar alumnos")
        print("3. Modificar email")
        print("4. Eliminar alumno")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            listar_alumnos()
        elif opcion == "3":
            modificar_email()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción inválida.")

# Ejecutamos el programa
menu()

