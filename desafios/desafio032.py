ano = int(input('INFORME QUALQUER ANO: '))
if ano % 4 == 0:
    if ano % 100 == 0 and not ano % 400 == 0:
        print('NÃO É BISSEXTO')
    else:
        print('É BISSEXTO')
else:
    print('NÃO É BISSEXTO')
