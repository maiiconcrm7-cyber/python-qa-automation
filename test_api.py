
import requests


def test_api_status_200():
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    assert resposta.status_code == 200


def test_api_nome_usuario():
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    dados = resposta.json()

    assert dados["name"] == "Leanne Graham"


def test_api_email_usuario():
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    dados = resposta.json()

    assert dados["email"] == "Sincere@april.biz"

def test_usuario_inexistente():
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/users/999999",
        timeout=10
    )

    assert resposta.status_code == 404

def test_api_tempo_resposta():
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    assert resposta.status_code == 200
    assert resposta.elapsed.total_seconds() < 3

def test_api_tipos_dados():
    resposta = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10
    )

    assert resposta.status_code == 200

    usuario = resposta.json()

    assert isinstance(usuario["id"], int)
    assert isinstance(usuario["name"], str)
    assert isinstance(usuario["email"], str)

def test_api_criar_usuario():
    url = "https://jsonplaceholder.typicode.com/users"

    novo_usuario = {
        "name": "Carlos Silva",
        "email": "carlos@teste.com"
    }

    resposta = requests.post(
        url,
        json=novo_usuario,
        timeout=10
    )

    assert resposta.status_code == 201

    dados = resposta.json()

    assert dados["name"] == "Carlos Silva"
    assert dados["email"] == "carlos@teste.com"

def test_api_atualizar_usuario():
    url = "https://jsonplaceholder.typicode.com/users/1"

    usuario_atualizado = {
        "id": 1,
        "name": "Carlos Atualizado",
        "email": "carlos@teste.com"
    }

    resposta = requests.put(
        url,
        json=usuario_atualizado,
        timeout=10
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["name"] == "Carlos Atualizado"
    assert dados["email"] == "carlos@teste.com"

def test_api_excluir_usuario():
    url = "https://jsonplaceholder.typicode.com/users/1"

    resposta = requests.delete(
        url,
        timeout=10
    )

    assert resposta.status_code == 200
