salario = float(input('Salário: '))
if salario > 1250.00:
    salario = salario + (salario * 0.1)
    print(f'Seu salário com aumento é de R$ {salario:.2f}')
else:
    salario = salario + (salario * 0.15)
    print(f'Seu salário com aumento é de R$ {salario:.2f}')
