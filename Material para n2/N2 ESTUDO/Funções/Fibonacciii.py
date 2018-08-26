'''10)	A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Escreva um programa modularizado que apresente a série de Fibonacci até o n-ésimo termo (n > 0).
O seu programa deve contar uma função que lê um número inteiro e positivo, bem como uma função, chamada Fibonacci,
que recebe um inteiro e positivo n e retorna um inteiro e positivo,
representando n-ésimo termo.'''


def Le_numero():
    numero = int(input("Dgt o termo: "))
    return numero

def Fibonacci(numero):
    if numero <= 1:
        return numero
    else:
        return (Fibonacci(numero - 1) + Fibonacci(numero - 2))

numero = Le_numero()

fib = print(Fibonacci(numero))


