
import pytest
from cadastro import cadastrar_usuario


@pytest.mark.parametrize("idade, esperado", [
    (15, "Erro: idade mínima de 18 anos"),
    (16, "Erro: idade mínima de 18 anos"),
    (17, "Erro: idade mínima de 18 anos"),
    (18, "Cadastro realizado com sucesso"),
    (19, "Cadastro realizado com sucesso"),
    (25, "Cadastro realizado com sucesso"),
    (60, "Cadastro realizado com sucesso"),
])
def test_validar_idade(idade, esperado):
    resultado = cadastrar_usuario("Carlos", idade)
    assert resultado == esperado
