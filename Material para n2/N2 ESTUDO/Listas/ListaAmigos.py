def msg():
    print("-=-="*20)
    print("LISTA DE AMIGOS :)")
msg()

def op():
    print("\n")
    print("(1) - Cadastrar um amigo no final da lista")
    print("(2) - Mostrar o nome de todos na lista")
    print("(3) Cadastrar um amigo no início da lista")
    print("(4) Remover um nome")
    print("(5) Substituir um nome")
    print("(6) Mostrar o número total de amigos cadastrados")
    print("(7) Colocar os nomes dos amigos em ordem alfabética")
    print("(8) - Sair da Lista ""\n")
    tipo = int(input("Digite uma opção: "))
    return tipo

def nome_lista_final():  # 1
    nome = str(input("Digite o nome a ser cadastrado no final: "))
    print("\n")
    lista.append(nome)
    return lista

def mostrar_lista():     # 2
    print(lista)
    print("\n")
    return lista

def nome_lista_inicio():  # 3
    nome = str(input("Digite um nome a ser cadastrado no começo: "))
    lista.insert(0,nome)
    return lista

def remover_nome_lista(): # 4
    id = int(input("Digite o indice a ser removido da lista: "))
    del lista[id]
    return lista

def sub_nome_lista():   # 5
    id = int(input("Digite o indice a ser substituido da lista: "))
    nome = str(input("Digite o novo nome: "))
    lista[id] = nome
    return lista

def total_lista():   # 6
    print("Tamanho total da lista",len(lista))
    return lista

def ordem_lista():   # 7
    lista.sort()
    return lista

def sair_lista():        # 8
    print("Voce saiu")
    return lista

lista = []

while True:

    escolha = op()

    if escolha == 1:
        lista = nome_lista_final()

    if escolha == 2:
        lista = mostrar_lista()

    if escolha == 3:
        lista = nome_lista_inicio()

    if escolha == 4:
        lista = remover_nome_lista()

    if escolha == 5:
        lista = sub_nome_lista()

    if escolha == 6:
        lista = total_lista()

    if escolha == 7:
        lista = ordem_lista()

    if escolha == 8:
        lista = sair_lista()
        break




