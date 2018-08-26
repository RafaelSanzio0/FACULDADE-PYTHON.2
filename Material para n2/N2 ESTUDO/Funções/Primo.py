#FUNÇAO QUE RETORNA PRIMO

def Le_numero():
    numero = int(input("dgt o numero: "))
    return numero

def Primo(numero):
    div = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            div += 1
        else:
            continue
    if div == 2:
        print("é primo")
    else:
        print("nao é primo")

numero = Le_numero()
numero_primo = Primo(numero)


