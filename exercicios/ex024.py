cidade = input('Informe uma cidade: ')
cidade = cidade.upper().split()
resposta = 'SANTO' in cidade[0]
print(f'Cidade começa com SANTO?: {resposta}')
