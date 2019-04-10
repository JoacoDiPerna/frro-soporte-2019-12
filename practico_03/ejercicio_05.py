# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from getpass import getuser
import sqlite3


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    conn = sqlite3.connect('C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    sql = "UPDATE personas SET nombre = ?, fechaNacimiento = ?, DNI = ?, altura = ?  WHERE id_persona=?"
    cur = conn.cursor()
    cur.execute(sql, (nombre, nacimiento, dni, altura, id_persona))
    rta = cur.rowcount
    cur.close()
    conn.commit()
    conn.close()
    print(rta)
    return True if rta > 0 else False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16 00:00:00', 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False


if __name__ == '__main__':
    pruebas()
