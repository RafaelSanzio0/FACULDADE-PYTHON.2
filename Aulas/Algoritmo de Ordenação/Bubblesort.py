# Youtube

lista = [50,40,33,300,543,21,2]
tamanho_lista = len(lista)

for i in range(tamanho_lista):
    troca = False
    for j in range(1,tamanho_lista):

        if lista[j] < lista[j-1]:  # verifica se o numero sucessor é menor que o antecessor
            lista[j] , lista[j-1] = lista[j-1] , lista[j]
            troca = True

    if not troca:
        break

print(lista)

