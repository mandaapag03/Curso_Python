frase = input('Escreva alguma frase: ').strip()
frase = frase.lower()
qnt_a = frase.count('a')
print(f'A letra "a" aparece {qnt_a} vezes')
posicao_1_a = frase.find('a') + 1
print(f'O "a" aparece pela primeira vez na posição {posicao_1_a}')
posicao_n_a = frase.rfind('a') + 1
print(f'O "a" aparece pela última vez na posição {posicao_n_a}')
