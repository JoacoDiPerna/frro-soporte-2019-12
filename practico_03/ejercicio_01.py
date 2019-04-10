# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
from getpass import getuser


def crear_tabla():
    conn = sqlite3.connect('C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS `personas` ( \
                                            `id_persona` INTEGER PRIMARY KEY AUTOINCREMENT,\
                                            `nombre` VARCHAR(30) NULL, \
                                            `fechaNacimiento` DATETIME NULL, \
                                            `DNI` INT NULL, \
                                            `altura` INT NULL); ')
    cur.close()
    conn.commit()
    conn.close()


def borrar_tabla():
    conn = sqlite3.connect('C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE `personas`')
    cur.close()
    conn.commit()
    conn.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()

    return func_wrapper


crear_tabla()
