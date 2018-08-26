# importa a biblioteca pygame
import pygame

# importando o time
import time

# inicializa as módulos dessa biblioteca;
pygame.init()

# seta o tamanho da janela
screen = pygame.display.set_mode((600,400))

# define um titulo na janela
pygame.display.set_caption("Ola mundo")

# troca a cor da janela para branco
screen.fill((255,255,255))

# CORES
branco = (255,255,255)
verde = (0,255,0)
preto = (0,0,0)
vermelho = (255,0,0)
azul = (0,0,255)

# COMPRIMENTOS
começo = [0,0]
fim = [50,30]
largura = 5
segmento = [[0,80],[50,90],[200,80],[220,30]]
começo1 = [0,50]
fim1 = [50,80]
largura1 = 1
retangulo = (150,10,50,20)
retangulo1 = (75,10,50,20)
borda = 2
elipse = (300,10,50,20)
elipse1 = (225,10,50,20)
poli = [[100,100],[0,200],[200,200]]
circu = [60,250]
raio = 40

# COMANDOS
pygame.draw.line(screen,verde,começo,fim,largura) # 1
pygame.draw.lines(screen,preto,False,segmento,largura) # 2
pygame.draw.aaline(screen,verde,começo1,fim1,largura1) # 3
pygame.draw.rect(screen,preto,retangulo) # 4
pygame.draw.rect(screen,preto,retangulo1,borda) # 5
pygame.draw.ellipse(screen,vermelho,elipse) # 6
pygame.draw.ellipse(screen,vermelho,elipse1,borda) # 7
pygame.draw.polygon(screen,preto,poli,borda) # 8
pygame.draw.circle(screen,azul,circu,raio) # 9

# atualiza a cor da janela
pygame.display.flip()

# tempo da janela aberta
time.sleep(5)

