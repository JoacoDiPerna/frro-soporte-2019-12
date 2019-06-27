# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import (
    NegocioSocio,
    DniRepetido,
    LongitudInvalida,
    MaximoAlcanzado,
)


class TestsNegocio(unittest.TestCase):
    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre="Juan", apellido="Perez")
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        # valida regla
        valido = Socio(dni=45678912, nombre="Luís", apellido="Lopez")
        self.assertTrue(self.ns.regla_1(valido))

        # DNI socio repetido
        invalido = Socio(dni=12345678, nombre="Juan", apellido="Perez")
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre="Juan", apellido="Perez")
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre="J", apellido="Perez")
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre="Juan", apellido="Perez")
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre="Juan Jose Facundo", apellido="Perez")
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre="Juan", apellido="Perez")
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre="Juan", apellido="P")
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre="Juan", apellido="Perez")
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre="Juan", apellido="Perez Alvarez Molina")
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # valida regla
        socio = Socio(dni=45678912, nombre="Luís", apellido="Lopez")
        self.ns.alta(socio)
        self.assertTrue(self.ns.regla_3())

        # número de socios mayor a 2
        socio = Socio(dni=12378945, nombre="Luisa", apellido="Molina")
        self.ns.alta(socio)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        pass

    def test_buscar(self):
        pass

    def test_buscar_dni(self):
        pass

    def test_todos(self):
        pass

    def test_modificacion(self):
        pass


if __name__ == "__main__":
    tn = TestsNegocio()
    tn.setUp()
    tn.test_alta()
    tn.test_regla_1()
    tn.test_regla_2_nombre_menor_3()
    tn.test_regla_2_nombre_mayor_15()
    tn.test_regla_2_apellido_menor_3()
    tn.test_regla_2_apellido_mayor_15()
    tn.test_regla_3()
    tn.tearDown()
