# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
from practico_03.ejercicio_01 import create_connection
from practico_03.ejercicio_01 import reset_tabla
from getpass import getuser


def agregar_persona(nombre, nacimiento, dni, altura):
    conn = create_connection(
        'C:\\Users\\' + getuser() + '\\Desktop\\tps_python.db')
    sql = ''' INSERT INTO personas(Nombre, FechaNacimiento, DNI, Altura)
                 VALUES(?,?,?,?) '''
    values = (nombre, datetime.datetime.strftime(
        nacimiento, "%Y-%m-%d"), dni, altura)
    cur = conn.cursor()
    cur.execute(sql, values)
    cur.close()
    conn.commit()
    conn.close()
    return cur.lastrowid


@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona(
        'marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
