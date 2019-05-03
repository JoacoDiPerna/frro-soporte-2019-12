# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
from practico_03.ejercicio_01 import create_connection
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from getpass import getuser


def buscar_persona(id_persona):
    conn = create_connection(
        'C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    sql = "SELECT * FROM personas WHERE id_persona=? ORDER BY id_persona ASC"
    cur = conn.cursor()
    cur.execute(sql, (id_persona,))
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return False if not rows else rows[0]


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', '1988-05-15', 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
