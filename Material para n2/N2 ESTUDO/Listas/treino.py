lista = []

def escolha_t():
    tamanho = int(input("Digite o tamanho da lista: "))
    return tamanho


def lista_feita(tamanho):
    for i in range(1,tamanho+1):
        numero = int(input("dgt os numero: "))
        lista.append(numero)

    return [numero for numero in lista if numero % 2 == 0]

tamanho = escolha_t()
lista = print(lista_feita(tamanho))





