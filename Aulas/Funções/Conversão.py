# DEFININDO CADA TAREFA DE CADA FUNÇÃO

def exibeMSG():
    print("-=-=-=" * 20)
    print("Programa de conversão de temperatura / informe F - de Fahreint para Celsius e C - de Celsius para Fahreint")
exibeMSG()

def getConverTo():
    op = str(input("Escolha o tipo de conversão desejada: ")).upper()
    while op.upper() != "F" and op.upper() != "C":
        op = str(input("Digite novamente: "))
    return op

def exibeFahrenheitTOCelsius(start):
    end = (start - 32) / 1.8
    return end

def exibeCelsiusTOFahrenheit(start):
    end = (start * 1.8) + 32
    return end

# PROGRAMA COMEÇA A RODAR AQUI

if getConverTo() == "F":
    temp = float(input("Informe a temperatura: "))
    a = exibeFahrenheitTOCelsius(temp)
    print(format(a,".2f"))
else:
    temp = float(input("Informe a temperatura: "))
    a = exibeCelsiusTOFahrenheit(temp)
    print(format(a,".2f"))











