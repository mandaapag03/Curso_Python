from random import randint
from time import sleep
n = randint(0,5)
print('Pensando em um número...')
sleep(3)
user = int(input('Advinhe em que número eu pensei: '))
if user == n:
    print('PARABÉNS!! VOCÊ ACERTOU!')
else:
    print('Você errou, humano insolente!')
