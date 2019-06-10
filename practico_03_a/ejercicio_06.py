# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from practico_03_a.ejercicio_01 import borrar_tabla, crear_tabla, meta, engine
from sqlalchemy import Table, Column, INTEGER, DATE, ForeignKey

pesos = Table('pesos', meta, Column('id_peso', INTEGER, primary_key=True), Column('id_persona', INTEGER, ForeignKey('personas.id_persona'), nullable=False), Column(
    'fecha', DATE, nullable=False), Column('peso', INTEGER, nullable=False))


def crear_tabla_peso():
    pesos.create(engine)


def borrar_tabla_peso():
    pesos.drop(engine)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
