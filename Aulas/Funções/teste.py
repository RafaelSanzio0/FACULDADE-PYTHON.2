def opcaoPagamento():
    print("Opções de pagamento:\n 1. A vista com 10% de desconto\n 2. 2x sem juros\n 3. Parcelado")
    opcao = int(input("Digite 1, 2 ou 3: "))
    return (opcao)


def aVista(preco):
    precoParcela = (preco * 10) / 100
    valorFinal = preco - precoParcela
    return (valorFinal)


def duasVezesSemJuros(preco):
    precoParcela = preco / 2
    return (precoParcela)


def parcelado(preco, numeroParcelas):
    if (100 > preco):
        precoParcela = preco / numeroParcelas
    else:
        juros = preco * 3 / 100
        precoParcela = juros + (preco / numeroParcelas)
    return (precoParcela)


a = opcaoPagamento()
preco = float(input("Digite o valor da compra: "))

if (a == 1):
    b = aVista(preco)
    print("O valor total da compra é: R$ %.2f" % b)
elif (a == 2):
    b = duasVezesSemJuros(preco)
    print("O valor total é R$ %.2f" % preco, " e o valor de cada parcela é R$ %.2f" % b)
else:
    parcelas = int(input("Digite a quantidade de parcelas: "))
    b = parcelado(preco, parcelas)
    print("O valor da compra é R$ %.2f" % preco, " e o valor de cada parcela é R$ %.2f" % b,
          " sendo 3% de juros ao mes")