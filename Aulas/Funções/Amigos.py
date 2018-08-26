#OBS: PROFESSORA, O ITEM 5 EU NAO CONSEGUI FAZER

def msg():
    print("\n""Programa LISTAS DE AMIGOS""\n")
msg()


def opções():
    print("(0) Sair do programa")
    print("(1) Cadastrar um amigo (no final da lista)")
    print("(2) Mostrar os nomes de todos os amigos")
    print("(3) Cadastrar um amigo(inicio da lista)")
    print("(4) Remover um nome")
    print("(5) Substituir um nome")
    print("(6) Mostrar o numero total de amigos")
    print("(7) Colocar o nome dos amigos e ordem alfabética")
    op = int(input("\n""Digite a sua opção: "))
    return op


def cadastro(lista):   # 1
    nome = str(input("Digite o nome do amigo(será cadastrado no final):"))
    print("-=-="*10)
    lista.append(nome)
    return lista


def saída(lista):  # 2
    print(lista)
    return lista


def cadastroo(lista): # 3
    nome = str(input("Digite o nome do amigo(será cadastrado no inicio):"))
    print("-=-="*10)
    lista.insert(0,nome)
    return lista


def remov(lista):   # 4
    remove = lista.remove(input())
    return lista


def mostrar(lista):  # 6
    print(len(lista))
    return lista


def ordem(lista):   # 7
    ordem = lista.sort()
    return lista


# INICIANDO O PROGRAMA

rodando = True
lista = []

while rodando:
    x = opções()

    if x == 0:
        print("VOCE SAIU DO PROGRAMA")
        break

    if x == 1:
        print("-=-="*10)
        print("OPÇAO 1 SELECIONADA")
        lista = cadastro(lista)

    if x == 2:
        print("OPÇAO 2 SELECIONADA")
        lista = saída(lista)
        print("-=-="*10)

    if x == 3:
        print("OPÇÃO 3 SELECIONADA")
        lista = cadastroo(lista)

    if x == 4:
        print("OPÇAO 4 SELECIONADA")
        print("Digite o nome do conteúdo a ser apagado: ")
        lista = remov(lista)
        print(lista)

    if x == 6:
        print("OPÇÃO 6 SELECIONADA")
        print("Quantidade de amigos cadastrados")
        lista = mostrar(lista)
        print("-=-="*10)

    if x == 7:
        print("OPÇAO 7 SELECIONADA")
        print("Todos os nomes foram colocados em ordem alfabética")
        lista = ordem(lista)
        print(lista)
        print("-=-="*10)














