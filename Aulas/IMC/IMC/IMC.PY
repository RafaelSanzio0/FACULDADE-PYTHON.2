# RAFAEL SANZIO

def msg():
    print("Este programa calcula o IMC""\n")
msg()

def IMC(peso,altura):
    formula = peso/altura**2
    return formula

op = str(input("Digite o sexo da pessoa: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = IMC(peso,altura)

if op.upper() == "F":
    if imc < 19.1:
        print("ABAIXO DO PESO")
    elif imc >= 19.1 and imc <= 25.8:
        print("NO PESO NORMAL")
    elif imc > 25.8 and imc <= 27.3:
        print("POUCO ACIMA DO PESO")
    elif imc > 27.3 and imc <= 32.3:
        print("ACIMA DO PESO IDEAL")
    elif imc < 32.3:
        print("OBESO")

elif op.upper() == "M":
    if imc < 20.7:
        print("ABAIXO DO PESO")
    elif imc >= 20.7 and imc <= 26.4:
        print("NO PESO NORMAL")
    elif imc > 26.4 and imc <= 27.8:
        print("PPOUCO ACIMA DO PESO")
    elif imc > 27.8 and imc <= 31.1:
        print("ACIMA DO PESO IDEAL")
    elif imc > 31.1:
        print("OBESO")