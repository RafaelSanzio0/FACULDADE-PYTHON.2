def opçao():
    print("\n(1) Cadastrar um amigo (no final da lista)")
    print("(2) Mostrar nome de todos os amigos")
    print("(3) Cadastrar um amigo (inicio da lista)")
    print("(4) Remover um nome")
    print("(5) Substituir um nome")
    print("(6) Mostrar o numero total de amigos cadastrados")
    print("(7) Colocar o nome dos amigos em ordem alfabetica")
    print("(0) Sair do Programa")
    opcao = int(input("Digite um valor do menu: "))
    return opcao
print("-=-="*10)

def cadastro(lista): # 1
    nome = str(input("Digite o nome do amigo(será cadastrado no final): \n"))
    lista.append(nome)
    return lista

def mostrar(lista): # 2
    print(lista)

def cadastroo(lista): # 3
    nome = str(input("Digite o nome do amigo(será adicionado no começo): "))
    lista.insert(0,nome)
    return lista

def remov(lista): # 4
    del lista[0]
    return lista

def total(lista): # 6
    lista = len(lista)
    return lista

#INICIO DO PROGRAMA
x = True
lista = []

while x:
    x = opçao()
    if x == 0:
        print("Voce saiu do menu")
    if x == 1:
        print("Nome do amigo a ser selecionado: ")
        lista = cadastro(lista)
    if x == 2:
        print("Amigos cadastrados")
        print(lista)
    if x == 3:
        print("Nome do amigo a ser selecionado: ")
        lista =cadastroo(lista)
    if x == 4:
        print("Um nome será removido")
        lista = remov(lista)
    if x == 6:
        print("O total de amigos é")
        lista = len(lista)













