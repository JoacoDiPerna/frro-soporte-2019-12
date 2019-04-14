# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
from practico_03.ejercicio_01 import create_connection
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_06 import reset_tabla
from getpass import getuser


def agregar_peso(id_persona, fecha, peso):
    if buscar_persona(id_persona) and existe_registro_posterior(id_persona, fecha):
        conn = create_connection(
            'C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
        sql = ''' INSERT INTO peso(idPersona, fecha, peso)
                     VALUES(?,?,?) '''
        values = (id_persona, datetime.datetime.strftime(
            fecha, "%Y-%m-%d"), peso)
        cur = conn.cursor()
        cur.execute(sql, values)
        cur.close()
        conn.commit()
        conn.close()
        return cur.lastrowid
    else:
        return False


def existe_registro_posterior(id_persona, fecha):
    conn = create_connection(
        'C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    sql = "SELECT fecha FROM peso WHERE idPersona=? ORDER BY fecha DESC"
    cur = conn.cursor()
    cur.execute(sql, (id_persona,))
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    if rows:
        if rows[0][0] > fecha.strftime("%Y-%m-%d"):
            return False
        else:
            return True
    else:
        return True


@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) is False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) is False


if __name__ == '__main__':
    pruebas()
