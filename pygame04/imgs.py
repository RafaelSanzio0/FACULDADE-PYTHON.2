import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Carregando imagem")
screen.fill((0,0,0))

x = 1
y = 1


pygame.time.delay(5000)

x = 0
lista = [pygame.image.load("boneco1.png"),pygame.image.load("boneco2.png"),pygame.image.load("boneco3.png"),pygame.image.load("boneco4.png")]
i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,255,255))
    screen.blit(lista[i],x(100))
    i += 1
    if i == 3:
        i = 0

    x += 1

    if x > 600:
        x -= 600
    pygame.display.update()






