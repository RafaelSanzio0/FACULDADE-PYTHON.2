import pygame, sys # IMPORTANDO O PYGAME

def main():    # FUNÇÃO PRINCIPAL
    pygame.init()  # INICIALIZA AS BIBLIOTECA
    tela = pygame.display.set_mode((1240,640)) # RELOSUÇÃO DA TELA
    pygame.display.set_caption("Projeto do Game")  # DEFINE O TITULO
    relogio = pygame.time.Clock() # FRAMES
    branco = (255,255,255)
    verde = (0,255,0)
    azul = (0,0,255)
    vermelho = (255,0,0)
    tamanho = (450,225)
    tamanho2 = (250,200)
    ret = pygame.Rect(10,10,55,55) # OBJETO
    imagem_fundo = pygame.image.load("gamer.jpg")    # CRIA IMAGEM
    sair = False

    while sair != True: # EM QUANTO SAIR FOR FALSE O PROGRAMA RODA
        for event in pygame.event.get(): # VARIAVEL EVENT RECEBENDO UM EVENTO
            if event.type == pygame.QUIT: # SE MEU EVENTO FOR IGUAL SAIR
                sair = True # ELE SAI

            #if event.type == pygame.MOUSEBUTTONDOWN: # SE EU CLICAR
                #ret = ret.move(10,10) # ELE MOVIMENTA

            if event.type == pygame.MOUSEMOTION: # ELE MOVIMENTA APENAS PASSANDO O MOUSE
                ret = ret.move(5,-5)

            if event.type == pygame.KEYDOWN: # VERIFICA SE ALGUMA TECLA FOI PRESSIONADA
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10,0)

                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10,0)

                if event.key == pygame.K_UP:
                    ret.move_ip(0,-10)

                if event.key == pygame.K_DOWN:
                    ret.move_ip(0,10)

                if event.key == (pygame.K_DOWN + pygame.K_RIGHT):
                    ret.move_ip(-10,-10)

                if event.key == (pygame.K_LEFT + pygame.K_UP):
                    ret.move_ip(10,10)


        relogio.tick(60) # DEFINE O FPS
        tela.blit(imagem_fundo, (0, 0))
        (ret.left,ret.top) = pygame.mouse.get_pos()
        pygame.draw.rect(tela, vermelho, ret,2)
        pygame.display.update() # DEFINE ATT PARA O CODIGO


    pygame.quit() # COMANDO DE SAÍDA

main()
