nome = input('Nome Completo: ')
nome = nome.upper().split()
resposta = 'SILVA' in nome
print(f'Tem Silva? R: {resposta}')
