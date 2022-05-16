import pygame
import emoji
print(emoji.emojize(':musical_note:'), 'Mais de Nós - Ana Gabriela', emoji.emojize(':musical_note:'))
# inicia o pygame
pygame.init()
# chamar o mixer para carregar a musica
pygame.mixer.music.load('ex021.mp3')
# tocar a música
pygame.mixer.music.play()
input()
# para fazer o programa esperar de tocar a msc para parar o programa
pygame.event.wait()
