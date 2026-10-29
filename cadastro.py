
def cadastrar_usuario(nome, idade):
    if nome == "":
        return "Erro: nome obrigatório"

    if idade < 18:
        return "Erro: idade mínima de 18 anos"

    return "Cadastro realizado com sucesso"


print(cadastrar_usuario("Carlos", 25))
print(cadastrar_usuario("", 30))
print(cadastrar_usuario("Ana", 16))
