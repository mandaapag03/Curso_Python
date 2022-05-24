from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade > 20:
    print('Categoria: MASTER')
else:
    if idade <= 9:
        print('Categoria: MIRIM')
    elif idade <= 14:
        print('Categoria: INFANTIL')
    else:
        print('Categoria: SÊNIOR')
        
