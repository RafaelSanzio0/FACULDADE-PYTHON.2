import pygame  # IMPORTANDO O PYGAME

def main():    # FUNÇÃO PRINCIPAL
    pygame.init()  # INICIALIZA AS BIBLIOTECA
    tela = pygame.display.set_mode((600,400)) # RELOSUÇÃO DA TELA
    pygame.display.set_caption("Projeto do Game")  # DEFINE O TITULO
    relogio = pygame.time.Clock() # FRAMES
    branco = (255,255,255)
    verde = (0,255,0)
    azul = (0,0,255)
    vermelho = (255,0,0)
    tamanho = (450,225)
    tamanho2 = (250,200)
    ret = pygame.Rect(10,10,55,55) # OBJETO
    sup = pygame.Surface(tamanho,) # CRIANDO MINHA SUPERFICE
    sup2 = pygame.Surface(tamanho2,)
    sair = False

    while sair != True: # EM QUANTO SAIR FOR FALSE O PROGRAMA RODA
        for event in pygame.event.get(): # VARIAVEL EVENT RECEBENDO UM EVENTO
            if event.type == pygame.QUIT: # SE MEU EVENTO FOR IGUAL SAIR
                sair = True # ELE SAI

            #if event.type == pygame.MOUSEBUTTONDOWN: # SE EU CLICAR
                #ret = ret.move(10,10) # ELE MOVIMENTA

            #if event.type == pygame.MOUSEMOTION: # ELE MOVIMENTA APENAS PASSANDO O MOUSE
                #ret = ret.move(-10,-10)

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


        relogio.tick(30) # DEFINE O FPS
        tela.fill(branco) # COR DE FUNDO
        sup.fill(azul) # COR DE FUNDO (SUPERFICIE)
        sup2.fill(verde)
        tela.blit(sup,[75,75])   # CHAMA A SUPERFICIE
        tela.blit(sup2,[165,88])
        pygame.draw.rect(tela, vermelho, ret,2)
        pygame.display.update() # DEFINE ATT PARA O CODIGO


    pygame.quit() # COMANDO DE SAÍDA

main()


