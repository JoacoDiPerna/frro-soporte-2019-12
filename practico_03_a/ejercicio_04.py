# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
from practico_03_a.ejercicio_01 import reset_tabla, personas, engine
from practico_03_a.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    stmt = personas.select().where(personas.c.id_persona == id_persona)
    conn = engine.connect()
    result = conn.execute(stmt)
    row = result.fetchone()
    return False if row is None else row


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona(
        'juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
