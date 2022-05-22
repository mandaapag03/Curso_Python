n1, n2 = input('Informe 2 números: ').split()
n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
    
