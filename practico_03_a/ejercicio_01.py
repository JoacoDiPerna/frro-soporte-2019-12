# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, create_engine, Table, Column, VARCHAR, DATE, INTEGER
from sqlalchemy.orm import sessionmaker
from getpass import getuser

engine = create_engine('sqlite:///C:\\Users\\' +
                       getuser() + '\\Desktop\\tp3a_python.db', echo=True)
meta = MetaData()

personas = Table('personas', meta, Column('id_persona', INTEGER, primary_key=True), Column('nombre', VARCHAR(30), nullable=False), Column(
    'fecha_nacimiento', DATE, nullable=False), Column('dni', INTEGER, nullable=False), Column('altura', INTEGER, nullable=False))


def crear_tabla():
    # meta.create_all(engine)
    personas.create(engine)


def borrar_tabla():
    # meta.drop_all(engine)
    personas.drop(engine)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
