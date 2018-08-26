'''9)	Dado um número inteiro positivo, escreva um programa modularizado para calcular a soma de seus dígitos.
 O seu programa deve contar uma função que lê um número inteiro e positivo, bem como uma função,
 chamada somaDigitos, que recebe um inteiro e positivo n
e retorna um inteiro e positivo, representando a soma dos dígitos do número dado.'''

def Le_numero():
    numero = str(input("Dgt um numero: "))
    return numero

def soma_digito(numero):
    soma = 0
    for i in range(len(numero)):
        soma += int(numero[i])
    print("A soma dos dgts é",soma)

numero = Le_numero()
soma = soma_digito(numero)