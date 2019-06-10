# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
from practico_03_a.ejercicio_01 import reset_tabla, personas, engine


def agregar_persona(nombre, nacimiento, dni, altura):
    stmt = personas.insert().values(
        nombre=nombre, fecha_nacimiento=nacimiento, dni=dni, altura=altura)
    conn = engine.connect()
    result = conn.execute(stmt)
    return result.lastrowid


@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona(
        'marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
