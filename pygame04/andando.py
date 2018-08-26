import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Carregando imagem")
screen.fill((0,0,0))


while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            imagem = pygame.image.load("download.jpg")
        if event.key == pygame.K_2:
          print("b")
        if event.key == pygame.K_3:
          screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (150, 10, 50, 20))
        if event.key == pygame.K_4:
          screen.fill((255, 255, 255))