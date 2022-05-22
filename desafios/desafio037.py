num = int(input('Informe um número inteiro: '))
opcao = int(input('Para converter, digite (1 - Binário | 2 - Octal | 3 - Hexadecimal )'))
if opcao == 1:
    print(f'O número {num} em binário é {bin(num)}')
elif opcao == 2:
    print(f'O número {num} em octal é {oct(num)}')
elif opcao == 3:
    print(f'O número {num} em hexadecimal é {hex(num)}')
else:
    print('ERRO! Selecione uma opção válida!')
    
