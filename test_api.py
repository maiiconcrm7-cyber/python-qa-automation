
import requests
import pytest


# ==========================================
# CONFIGURACAO DA API
# ==========================================

BASE_URL = "https://jsonplaceholder.typicode.com"


# ==========================================
# FIXTURE - DADOS DO USUARIO
# ==========================================

@pytest.fixture
def usuario_api():
    resposta = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200, (
        f"Status inesperado: {resposta.status_code}"
    )

    return resposta.json()


# ==========================================
# TESTE 1 - STATUS HTTP 200
# ==========================================

def test_api_status_200():
    resposta = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200


# ==========================================
# TESTE 2 - NOME DO USUARIO
# ==========================================

def test_api_nome_usuario():
    resposta = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["name"] == "Leanne Graham", (
        f"Nome incorreto: {dados['name']}"
    )


# ==========================================
# TESTE 3 - EMAIL DO USUARIO
# ==========================================

def test_api_email_usuario():
    resposta = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["email"] == "Sincere@april.biz"


# ==========================================
# TESTE 4 - USUARIO INEXISTENTE
# ==========================================

def test_usuario_inexistente():
    resposta = requests.get(
        f"{BASE_URL}/users/999999",
        timeout=10
    )

    assert resposta.status_code == 404


# ==========================================
# TESTE 5 - TEMPO DE RESPOSTA
# ==========================================

def test_api_tempo_resposta():
    resposta = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200

    assert resposta.elapsed.total_seconds() < 3, (
        "API demorou mais de 3 segundos"
    )


# ==========================================
# TESTE 6 - TIPOS DE DADOS
# ==========================================

def test_api_tipos_dados():
    resposta = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200

    usuario = resposta.json()

    assert isinstance(usuario["id"], int)
    assert isinstance(usuario["name"], str)
    assert isinstance(usuario["email"], str)


# ==========================================
# TESTE 7 - CRIAR USUARIO (POST)
# ==========================================

def test_api_criar_usuario():
    novo_usuario = {
        "name": "Carlos Silva",
        "email": "carlos@teste.com"
    }

    resposta = requests.post(
        f"{BASE_URL}/users",
        json=novo_usuario,
        timeout=10
    )

    assert resposta.status_code == 201

    dados = resposta.json()

    assert dados["name"] == novo_usuario["name"]
    assert dados["email"] == novo_usuario["email"]


# ==========================================
# TESTE 8 - ATUALIZAR USUARIO (PUT)
# ==========================================

def test_api_atualizar_usuario():
    usuario_atualizado = {
        "id": 1,
        "name": "Carlos Atualizado",
        "email": "carlos@teste.com"
    }

    resposta = requests.put(
        f"{BASE_URL}/users/1",
        json=usuario_atualizado,
        timeout=10
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["name"] == usuario_atualizado["name"]
    assert dados["email"] == usuario_atualizado["email"]


# ==========================================
# TESTE 9 - EXCLUIR USUARIO (DELETE)
# ==========================================

def test_api_excluir_usuario():
    resposta = requests.delete(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert resposta.status_code == 200


# ==========================================
# TESTE 10 - ID COM FIXTURE
# ==========================================

def test_usuario_id_fixture(usuario_api):
    assert usuario_api["id"] == 1


# ==========================================
# TESTE 11 - NOME COM FIXTURE
# ==========================================

def test_usuario_nome_fixture(usuario_api):
    assert usuario_api["name"] == "Leanne Graham"


# ==========================================
# TESTE 12 - EMAIL COM FIXTURE
# ==========================================

def test_usuario_email_fixture(usuario_api):
    assert usuario_api["email"] == "Sincere@april.biz"
