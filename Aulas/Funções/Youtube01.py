def msg():
    print("ESTE PROGRAMA CALCULA O IMPOSTO DE DETERMINADO PRODUTO""\n")

msg()

def SomaImposto (taxaImposto,custo):
    aumento = ((taxaImposto/100) * custo) + custo
    return aumento

valor = float(input("Digite o valor do produto: "))
imposto = float(input("Digite o valor em % do aumento: "))

aumento = SomaImposto(imposto,valor)

print("Preço final do produto %.2d" %(aumento))


