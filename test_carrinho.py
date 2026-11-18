
import pytest

from carrinho import calcular_total


@pytest.mark.parametrize(
    "quantidade, esperado",
    [
        (1, 50),
        (2, 100),
        (3, 150),
        (0, "Erro: quantidade invalida"),
        (-1, "Erro: quantidade invalida"),
    ]
)
def test_calculo_carrinho(quantidade, esperado):
    resultado = calcular_total(50, quantidade)

    assert resultado == esperado, (
        f"Quantidade: {quantidade} | "
        f"Esperado: {esperado} | "
        f"Obtido: {resultado}"
    )
