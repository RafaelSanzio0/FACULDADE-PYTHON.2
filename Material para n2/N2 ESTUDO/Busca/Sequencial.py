def busca_seq(lista,x):              # função da busca sequencial
    for i in range(len(lista)):
        if lista[i] == x:
            return "valor encontrado %d na posição %d" % (x,i)
    return "numero não encontrado"

def add_lista(lista,valores):        # adiciona os valores a lista
    lista.append(valores)
    return lista

lista = []
tamanho = int(input("Digite o tamanho da lista: "))

while len(lista) < tamanho:       # add os valores de acordo com o tamanho especificado
  valores = int(input("digite os valores a serem add na lista: "))
  add_lista(lista,valores)

print(lista)

x = int(input("Dgt o valor para buscar na lista: "))

print(busca_seq(lista,x))