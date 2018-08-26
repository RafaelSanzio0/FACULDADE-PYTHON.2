def busca_binaria(lista,x):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        meio = (primeiro+ultimo)//2
        if lista[meio] == x:
            return meio
        else:
            if x < lista[meio]:
                ultimo = meio-1
            else:
                if x > lista[meio]:
                    primeiro = meio+1
    return "elemento nao encontrado"

def add_lista(lista,valores):
    lista.append(valores)
    return lista

lista = []
tamanho = int(input("Digite o tamanho da lista: "))

while len(lista) < tamanho:       # add os valores de acordo com o tamanho especificado
  valores = int(input("digite os valores a serem add na lista: "))
  add_lista(lista,valores)

print(lista)

x = int(input("Dgt o valor para buscar na lista: "))

print(busca_binaria(lista,x))