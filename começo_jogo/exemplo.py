# Importa as bibliotecas utilizadas
import sys, pygame
from random import *

# Inicializa a biblioteca pygame
pygame.init()

# Cria a surface
size = (800, 600)
screen = pygame.display.set_mode(size)

# Define um titulo para a janela
pygame.display.set_caption("Hello World")

# ----------------PARTE 2-------------------------------------

# Define as cores em RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Declara o vetor que controla a posicao X e Y do circulo
posicaoCirculo = [200, 30]

# Armazena num vetor a Velocidade de movimentacao do circulo
velocidadeCirculo = [5, 5]

# Utilizado para controlar a velocidade de quadros (de atualizaÃ§Ãµes da tela)
clock = pygame.time.Clock()

# VariÃ¡vel para iniciar a posiÃ§Ã£o do cÃ­rculo vermelho
criar = True

# VariÃ¡veis de posiÃ§Ã£o do cÃ­rculo vermelho
X_vermelho = 0
Y_vermelho = 0

# ----------------PARTE 3-------------------------------------

# Loop principal do jogo
while True:

    # Verifica se algum evento aconteceu
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT),
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT: sys.exit()

    # Verifica se alguma tecla foi pressionada
    pressed = pygame.key.get_pressed()

    # Verifica qual tecla (seta) foi pressionada e atualiza o vetor Posicao de acordo com a Velocidade
    if pressed[pygame.K_UP]: posicaoCirculo[1] -= velocidadeCirculo[1]
    if pressed[pygame.K_DOWN]: posicaoCirculo[1] += velocidadeCirculo[1]
    if pressed[pygame.K_LEFT]: posicaoCirculo[0] -= velocidadeCirculo[0]
    if pressed[pygame.K_RIGHT]: posicaoCirculo[0] += velocidadeCirculo[0]

    # Preenche a tela com cor preto
    screen.fill(BLACK)

    # Desenha um circulo branco na tela
    pygame.draw.circle(screen, WHITE, posicaoCirculo, 20)

    # Aqui Ã© setado a posiÃ§Ã£o inicial da bola vermelha
    if criar == True:
        X_vermelho = randint(20, 580)
        Y_vermelho = 20
        criar = False

    # Valores da bola vermelha Ã© atribuido
    posicaoCirculo2 = [X_vermelho, Y_vermelho]

    # Desenha o cÃ­rculo vermelho
    pygame.draw.circle(screen, RED, posicaoCirculo2, 10)

    # Velocidade de queda do cÃ­rculo Vermelho
    Y_vermelho += 5

    # Se o cÃ­rculo vermelho ultapassar a  tela ela Ã© reiniciada
    if Y_vermelho > 600:
        criar = True

    # Se o CÃ­rculo Branco encostar no CÃ­rculo Vermelho o cÃ­rculo vermelho Ã© reiniciado
    # CB: CÃ­rculo Branco    CV: CÃ­rculo Vermelho
    #        y + altura CB          y CV                    y CB                y + altura CV            x + largura CB           x CV                x CB                 x CV
    if (posicaoCirculo[1] + 20 >= Y_vermelho - 10 and posicaoCirculo[1] - 20 <= Y_vermelho + 10) and (
                posicaoCirculo[0] + 20 >= X_vermelho - 10 and posicaoCirculo[0] - 20 <= X_vermelho + 20):
        criar = True

    # Atualiza a tela visivel ao usuario
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(60)

