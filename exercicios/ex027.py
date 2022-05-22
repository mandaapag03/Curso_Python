nome = input('Nome completo: ').strip()
nome = nome.split()
primeiro = nome[0]
ultimo = nome[len(nome) - 1]
print(f'Primeiro: {primeiro}')
print(f'Último: {ultimo}')
