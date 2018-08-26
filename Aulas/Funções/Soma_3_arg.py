'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos'''

def soma (n1,n2,n3):
    soma = n1 + n2 + n3
    return soma

n1 = int(input("Dgt primeiro valor: "))
n2 = int(input("Dgt segundo valor: "))
n3 = int(input("Dgt terceiro valor: "))

print(soma(n1,n2,n3))

