def exibeMsg():
    print("-=-="*20)
    print("Este programa converte temperaturas / F - de Fahreint para Celsius e  C - de celsius para Farheint")

def getConverto():
    tipo = str(input("Informe o tipo de conversão que deseja: ")).upper()
    return tipo

def exibeFahrentiToCelsius(start):
    end = (start - 32)/1.8
    return end

def exibeCelsiustoFahreint(start):
    end = (start * 1.8) + 32
    return end

exibeMsg()

tipo = getConverto()

if tipo == "F":
    temp = float(input("Digite a temperatura: "))
    b = exibeCelsiustoFahreint(temp)
    print(b)

else:
    temp = float(input("Digite a temperatura: "))
    b = exibeFahrentiToCelsius(temp)
    print(b)




