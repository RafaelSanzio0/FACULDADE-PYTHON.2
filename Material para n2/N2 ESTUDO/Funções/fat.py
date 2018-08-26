'''8)	Faça um programa modularizado que calcule e apresente o fatorial de um número inteiro
 e natural fornecido pelo usuário.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1=120.
Por definição 0! = 1.
O seu programa deve contar uma função que lê um número inteiro e positivo,
bem como uma função, chamada fatorial, que recebe um inteiro e positivo n e retorna um inteiro e positivo,
 representando a soma dos dígitos do número dado.
'''

def Le_numero():
    numero = int(input("Digite um numero: "))
    return numero

def Fatorial(numero):
    fat = 1
    for i in range(1,numero+1):
        fat = fat * i
    print("%d! = %d" % (numero,fat))


numero = Le_numero()

fatorial = Fatorial(numero)



