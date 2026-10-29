
from cadastro import cadastrar_usuario


def test_cadastro_valido():
    assert cadastrar_usuario("Carlos", 25) == "Cadastro realizado com sucesso"


def test_idade_17_anos():
    assert cadastrar_usuario("Ana", 17) == "Erro: idade mínima de 18 anos"


def test_idade_18_anos():
    assert cadastrar_usuario("Pedro", 18) == "Cadastro realizado com sucesso"


def test_nome_vazio():
    assert cadastrar_usuario("", 30) == "Erro: nome obrigatório"
