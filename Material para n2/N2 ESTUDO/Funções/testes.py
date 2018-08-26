

def rfunc(n):
    if n == 0:
        return 0
    else:
        return rfunc(n - 1) + 2


numero = int(input())

rec = print(rfunc(numero))
