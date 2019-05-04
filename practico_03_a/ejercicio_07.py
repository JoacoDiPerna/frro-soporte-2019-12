# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from practico_03_a.ejercicio_01 import personas, engine
from practico_03_a.ejercicio_02 import agregar_persona
from practico_03_a.ejercicio_04 import buscar_persona
from practico_03_a.ejercicio_06 import reset_tabla, pesos
from sqlalchemy import desc


def agregar_peso(id_persona, fecha, peso):
    if buscar_persona(id_persona) and existe_registro_posterior(id_persona, fecha):
        stmt = pesos.insert().values(id_persona=id_persona, fecha=fecha, peso=peso)
        conn = engine.connect()
        result = conn.execute(stmt)
        return result.lastrowid
    else:
        return False


def existe_registro_posterior(id_persona, fecha):
    stmt = pesos.select().where(pesos.c.id_persona == id_persona).where(
        pesos.c.fecha >= datetime.datetime.strftime(fecha, "%Y-%m-%d"))
    conn = engine.connect()
    result = conn.execute(stmt)
    return False if result.fetchone() is not None else True


@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.date(1988, 5, 15), 80) is False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.date(2018, 5, 16), 80) is False


if __name__ == '__main__':
    pruebas()
