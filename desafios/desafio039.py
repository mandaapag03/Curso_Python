# Alistamento Militar
import datetime
ano = int(input('Informe seu ano de nascimento: '))
idade = datetime.date.today().year - ano
if idade == 18:
    print('É hora de se alistar!')
elif idade < 18:
    print(f'Você ainda deve se alistar')
    tr = 18 - idade
    if tr == 1:
        print(f'Falta {tr} ano, está quase!')
    else:
        print(f'Faltam {tr} anos!')
else:
    print(f'Já passou do prazo de você se alistar')
    tr = idade - 18
    if tr == 1:
        print(f'Tempo de atraso: {tr} ano')
    else:
        print(f'Tempo de atraso: {tr} anos')
