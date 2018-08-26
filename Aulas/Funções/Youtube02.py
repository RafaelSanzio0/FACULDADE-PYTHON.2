def msg():
    print("=-=-="*19)
    print("ESTE PROGRAMA CONVERTE AS HORAS NO FORMATO 24 PARA 12""\n")

msg()

def conv (horas):       #FUNÇÃO DA CONVERSÃO
    return horas - 12

def printConv (horas,minutos):      #FUNÇÃO DE SAÍDA
    if horas > 12:
        horas = conv(horas)
        print("%d:%d PM" % (horas,minutos))
    else:
        print("%d:%d AM" % (horas,minutos))

rodando = True

while rodando:
    horas = int(input("Digite a hora: "))
    while horas < 0 or horas > 24:
        print("Não existem horas neste formato, digite novamente!: ")
        horas = int(input("Digite a hora: "))
        minutos = int(input("Digite os minutos: "))
    while minutos < 0 or minutos > 60:
        print("Não Existem minutos neste formato, digite novamente!:")
        minutos = int(input("Digite os minutos: "))
    printConv(horas, minutos)
    rodando = bool(int(input("Deseja fazer uma nova conversão(1 - sim/0 - não): ")))














