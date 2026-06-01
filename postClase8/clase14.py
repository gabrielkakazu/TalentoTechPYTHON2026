import sqlite3

def crearDB():
    conexion = sqlite3.connect("alumnos14.db")
    print("Conexión establecida exitosamente.")
    conexion.close()

def crearTabla():
    conexion = sqlite3.connect("alumnos14.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parcial1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        apellido TEXT NOT NULL,
        nota FLOAT NOT NULL)
        ''')
    conexion.commit()
    print("Tabla parcial1 creada exitosamente")
    conexion.close()

registro = ("Gómez", 9.50)

def insertarRegistro(tupla):
    conexion = sqlite3.connect("alumnos14.db")
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO parcial1 (apellido, nota)
        VALUES (?, ?)
        ''', tupla
    )
    conexion.commit()
    conexion.close()
    print(f"Registro {tupla} agregado a la tabla")

recuperatorio = 6.5
id_alumno = 1

def modificarNota(nuevaNota, id):
    conexion = sqlite3.connect("alumnos14.db")
    cursor = conexion.cursor()
    cursor.execute('UPDATE parcial1 SET nota = ? WHERE id = ?', (nuevaNota, id))
    conexion.commit()
    conexion.close()
    print(f"Nota {nuevaNota} actualizada en registro con id {id}")

def borrarRegistro(id_borrar):
    conexion = sqlite3.connect("alumnos14.db")
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM parcial1 WHERE id = ?', (id_borrar,))
    conexion.commit()
    conexion.close()
    print(f"Registro con id {id_borrar} borrado de la tabla")


def consultarTabla():
    conexion = sqlite3.connect("alumnos14.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM parcial1')
    parciales = cursor.fetchall()
    for registro in parciales:
        print(f"ID: {registro[0]}, Apellido: {registro[1]}, Nota de parcial: {registro[2]:.2f}")
    conexion.close()

alumnos = [("Adan", 10.0), ("Baccarini", 5.5), ("Diaz", 2.0), ("Elenchi", 7.75), ("Zorro", 8.80)]


if __name__ == "__main__":
    crearDB()
    crearTabla()
    for alumno in alumnos:
        insertarRegistro(alumno)
    # modificarNota(recuperatorio, id_alumno)
    # borrarRegistro(id_alumno)
    consultarTabla()
    pass
