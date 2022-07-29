import pygame
from pygame.locals import *
from sys import exit # Função fecha a janela ao clicar no X

pygame.init()

x = 640
y = 480
tela = pygame.display.set_mode((x,y))
pygame.display.set_caption('Escape')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update() # atualiza a tela do jogo
    
