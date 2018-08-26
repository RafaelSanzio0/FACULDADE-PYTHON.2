import random

def jogar():

    apresentacao_mensagem()
    palavra_secreta = escolhendo_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta] # usar "_" para cada letra dentro da palavra secreta

    # VARIAVEIS
    enforcou = False
    acertou = False
    contador = 0
    erros = 0

    # JOGO
    while not enforcou and not acertou:

            chute = pede_chute()

            if chute in palavra_secreta: # se meu chute estiver dentro da palavra secreta
                chute_correto(chute,palavra_secreta,letras_acertadas)

            else:
                print("Voce errou, faltam {} tentativas".format(7-erros))
                erros += 1
                desenha_forca(erros)
            enforcou = erros == 7

            acertou = "_" not in letras_acertadas # se nao existe mais "_" na var letras_acertadas o game acaba
            print(letras_acertadas)

    if acertou:
         msg_win()
    else:
         msg_loser(palavra_secreta)

    contador += 1


# AQUI VOCE ENCONTRA TODAS AS FUNÇOES OU SEJA AS LINHAS DE CÓDIGOS DE CADA PARTEDO PROGRAMA

def apresentacao_mensagem():
    print("**" * 20)
    print("Jogo da forca")
    print("**" * 20)

def escolhendo_palavra_secreta():
    palavra_secreta = []
    arquivo = open("teste.txt", "r")  # abrindo meu arquivo txt para LEITURA (r)

    for letra in arquivo:  # para cada Letra dentro da var arquivo
        letra = letra.strip()
        palavra_secreta.append(letra)

    arquivo.close()  # logo depois que ele é lido , ele é limpado pelo close

    numero = random.randrange(0, len(palavra_secreta))
    palavra_secreta = palavra_secreta[numero]
    return palavra_secreta

def pede_chute():
    chute = str(input("Dgt uma letra: ")).strip().lower()
    return chute

def chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:  # varre cada LETRA na Palavra_secreta
        if letra == chute:
            letras_acertadas[index] = letra
        index += 1
