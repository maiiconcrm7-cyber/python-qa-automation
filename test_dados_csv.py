import csv
import pytest

from cadastro import cadastrar_usuario


def carregar_dados():
    with open("dados_teste.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


@pytest.mark.parametrize("dados", carregar_dados())
def test_cadastro_com_csv(dados):
    nome = dados["nome"]
    idade = int(dados["idade"])
    resultado_esperado = dados["resultado_esperado"]

    resultado = cadastrar_usuario(nome, idade)

    if resultado_esperado == "Sucesso":
        assert "sucesso" in resultado.lower()
    else:
        assert "erro" in resultado.lower()