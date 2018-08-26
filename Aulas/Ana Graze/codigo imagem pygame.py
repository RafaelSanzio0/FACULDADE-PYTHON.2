import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Carregando Imagem")
screen.fill((255, 255, 255))


image = pygame.image.load("googlelogo_color_272x92dp.png")
boneco1 = pygame.image.load("boneco1.png")
boneco2 = pygame.image.load("boneco2.png")
boneco3 = pygame.image.load("boneco3.png")
boneco4 = pygame.image.load("boneco4.png")







x=0
y = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 0, 0))        
    screen.blit(boneco1, (x,100))
    break



