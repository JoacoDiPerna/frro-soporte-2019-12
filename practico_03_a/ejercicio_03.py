# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
from practico_03_a.ejercicio_01 import reset_tabla, personas, engine
from practico_03_a.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    stmt = personas.delete().where(personas.c.id_persona == id_persona)
    conn = engine.connect()
    result = conn.execute(stmt)
    return True if result.rowcount >= 1 else False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona(
        'juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert borrar_persona(1123) is False


if __name__ == '__main__':
    pruebas()
