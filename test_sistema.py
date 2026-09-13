import pytest

from sistema import (
    registrar_producto,
    calcular_total,
    validar_producto
)


def test_registrar_producto_correctamente():
    producto = registrar_producto("Cuaderno", 8000, 2)

    assert producto["nombre"] == "Cuaderno"
    assert producto["precio"] == 8000
    assert producto["cantidad"] == 2


def test_calcular_total_correctamente():
    total = calcular_total(8000, 2)

    assert total == 16000


def test_validar_producto_correctamente():
    resultado = validar_producto("Cuaderno", 8000, 2)

    assert resultado is True