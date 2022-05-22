from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Pensando em um número entre 0 e 5...')
print('-=-' * 20)
sleep(3)
user = int(input('Adivinhe em que número eu pensei: '))
print('PROCESSANDO...')
sleep(3)
if user == n:
    print('PARABÉNS!! VOCÊ ACERTOU!')
else:
    print('Você errou, humano insolente!')
    print(f'O número era {n}')
print('...' * 20)
