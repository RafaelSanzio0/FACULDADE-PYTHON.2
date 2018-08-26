# Importa as bibliotecas utilizadas
import sys, pygame
from random import *

# Inicializa a biblioteca pygame
pygame.init()

# Cria a surface
size = (800, 600)
screen = pygame.display.set_mode(size)

# Define um titulo para a janela
pygame.display.set_caption("ABERTURA")

#carrega imagem de background
imagem_fundo = pygame.image.load("gamer.jpg")


# ----------------PARTE 2-------------------------------------

# Define as cores em RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

while True:

    # Verifica se algum evento aconteceu
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT),
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            sys.exit()


# Preenche a tela com cor preto
screen.fill(BLACK)

screen.blit(imagem_fundo(0,0))

# Atualiza a tela visivel ao usuario
pygame.display.update()



