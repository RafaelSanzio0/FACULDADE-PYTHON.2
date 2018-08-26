'''Escreva uma função não recursiva que receba como parâmetro uma lista de inteiros e
retorne como resposta a soma de todos os elementos da lista'''

lista = [10,20,30]

def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += int(elemento)

    print("A soma dos elementos é", soma)

soma = soma_elementos(lista)







