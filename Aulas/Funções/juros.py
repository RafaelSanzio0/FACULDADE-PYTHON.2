'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que
a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar
a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def valorPagamento(valor,dias):
    if dias == 0:
        valor * 1
    else:
        valor = valor * 1.03 + 0.01 * dias
    return valor

loop = True

ac_valor = 0
total = 0

while loop:
    valor = float(input("Dgt o valor: "))
    dias = int(input("Dias de atraso: "))
    print("O Valor a ser pago é: ",end=" ",)
    print(valorPagamento(valor,dias))
    ac_valor += 1
    print("-=-="*17)
    loop = bool(int(input("Dejesa continuar 1 - sim 0 - não?: ")))
    print("-=-="*17)

for i in range(ac_valor):
    total += valor

print("-=-="*17)
print("RELATÓRIO DO DIA""\n""Quantidade total de pagamentos recebidos %d e o total em dinheiro %.2f" % (ac_valor,total))

