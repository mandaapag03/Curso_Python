frase = input('Escreva alguma frase: ')
frase = frase.lower()
qnt_a = frase.count('a')
print(f'A letra "a" aparece {qnt_a} vezes')
posicao_1_a = frase.find('a')
print(f'O "a" aparece pela primeira vez na posição {posicao_1_a}')
posicao_n_a = frase.rfind('a')
print(f'O "a" aparece pela última vez na posição {posicao_n_a}')
