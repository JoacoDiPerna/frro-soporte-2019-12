# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from getpass import getuser
import sqlite3


def borrar_persona(id_persona):
    conn = sqlite3.connect('C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    sql = 'DELETE FROM personas WHERE id_persona=?'
    cur = conn.cursor()
    cur.execute(sql, (id_persona,))
    rta = cur.rowcount
    cur.close()
    conn.commit()
    conn.close()
    return True if rta == 1 else False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(1123) is False

if __name__ == '__main__':
    pruebas()
