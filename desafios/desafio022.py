nome = input('Nome Completo: ')
print(f'Maiúscula: {nome.upper()}')
print(f'Minúscula: {nome.lower()}')
length = len(nome.replace(' ',''))
print(f'N° de letras: {length}')
nome = nome.split()
primeiro_nome = nome[0]
print(f'N° de letras primeiro nome: {len(primeiro_nome)}')
