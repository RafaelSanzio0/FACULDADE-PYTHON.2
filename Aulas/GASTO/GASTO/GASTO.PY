# RAFAEL SANZIO

def msg():
    print("Este programa calcula o gasto total de um cliente""\n")
msg()

def opções():
    print("CARO CLIENTE, VC TEM AS SEGUINTES OOÇÕES DE PAGAMENTO:")
    print("1 - PARA A VISTA""\n""2 - PARA PARCELAMENTO EM 2X""\n3 - PARA PARCELAMENTO ENTRE 3 A 10X""\n")
opções()

def tipo():
    op = int(input("SELECIONE O TIPO DESEJADO: "))
    if op == 1:
        print("VOCE ESCOLHEU A OPÇAO DE PAGAR A VISTA""\n")
    if op == 2:
        print("VOCE ESCOLHEU A OPÇAO DE PAGAR EM 2X""\n")
    if op == 3:
        print("VOCE ESCOLHEU A OPÇÃO DE PAGAR ENTRE 3X A 10X""\n")
    return op

def Avista(preço):
    total = preço - (preço*0.10)
    return total

def DuasVezes(preço):
    total = preço/2
    return total

def TresAteDez(preço,parcelas):
    if preço > 100:
        juros = parcelas * 3/100
        total = juros+(preço/parcelas)
        return total
    else:
        total = preço/parcelas
        return total

#PROGRAMA COMEÇA A RODAR AQUI

x = tipo()
preço = float(input("Digite o preço do produto: "))

if x == 1:
    a = Avista(preço)
    print("O CLIENTE GASTOU R$ %.2f E O VALOR COM DESCONTO A VISTA FICOU R$ %.2f" % (preço,a))

elif x == 2:
    a = DuasVezes(preço)
    print("O CLIENTE GASTOU R$ %.2f PARCELADO EM 2X DE R$ %.2F" % (preço,a))
else:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    a = TresAteDez(preço,parcelas)
    print("O CLIENTE GASTOU R$ %.2f PARCELADO EM %d VEZES DE %.2f COM JUROS DE 3 POR CENTO AO MES " % (preço,parcelas,a))





