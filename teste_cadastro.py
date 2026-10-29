
from cadastro import cadastrar_usuario

# Teste 1 - Idade abaixo do limite
assert cadastrar_usuario("Carlos", 17) == "Erro: idade mínima de 18 anos"

# Teste 2 - Idade exatamente no limite
assert cadastrar_usuario("Ana", 18) == "Cadastro realizado com sucesso"

# Teste 3 - Idade acima do limite
assert cadastrar_usuario("Pedro", 19) == "Cadastro realizado com sucesso"

print("Todos os testes de limites passaram!")
