n1, n2 = input('Informe suas notas: ').split()
n1 = float(n1)
n2 = float(n2)
media = (n1 + n2)/2
print(f'Sua média é {media:.2f}')
if media >= 7:
    print('APROVADO!')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')
