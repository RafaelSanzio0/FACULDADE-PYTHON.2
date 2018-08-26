def cria_matriz(numero_linhas,numero_colunas):
    matriz = []

    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            valor = int(input("valores [" + str(i) + "][" + str(j) + "] = "))
            linha.append(valor)

        matriz.append(linha)

    return matriz


def le_matriz():
    numero_linha = int(input("Dgt o numero de linhas: "))
    numero_coluna = int(input("Dgt o numero de colunas: "))
    return cria_matriz(numero_linha,numero_coluna)

m = le_matriz()

print(m)













