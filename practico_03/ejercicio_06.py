# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla
from getpass import getuser
import sqlite3


def crear_tabla_peso():
    conn = sqlite3.connect('C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS peso (idPeso INTEGER PRIMARY KEY AUTOINCREMENT, \
                                                  idPersona INTEGER, \
                                                  fecha DATETIME NULL, \
                                                  peso INT NULL, \
                                                  CONSTRAINT fk_personas \
                                                  FOREIGN KEY (idPersona) \
                                                  REFERENCES personas(id_persona)); ')
    cur.close()
    conn.commit()
    conn.close()


def borrar_tabla_peso():
    conn = sqlite3.connect('C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE peso')
    cur.close()
    conn.commit()
    conn.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()

    return func_wrapper
