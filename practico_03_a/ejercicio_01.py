# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, VARCHAR, DATE, INTEGER, DECIMAL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def Persona(Base):
    __tablename__ = 'personas'
    id_persona = Column(INTEGER, primary_key=True)
    nombre = Column(VARCHAR(30), nullable=False)
    fecha_nacimiento = Column(DATE, nullable=False)
    dni = Column(INTEGER, nullable=False)
    altura = Column(DECIMAL, nullable=False)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def crear_tabla():
    Base.metadata.create_all(engine)


def borrar_tabla():
    table = metadata.tables.get('personas')
    if table is not None:
        logging.info(f'Deleting {'personas'} table')
        base.metadata.drop_all(engine, [table], checkfirst=True)

# no modificar


def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


crear_tabla()
borrar_tabla()
