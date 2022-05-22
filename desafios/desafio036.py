casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Em quantos anos você vai pagar? '))

prestacao = casa / (anos*12)
if prestacao < (salario * 0.30):
    print(f'Você é elegível para realizar o empréstimo')
    print(f'O valor da sua prestação vai ser de R$ {prestacao:.2f} em {anos*12} meses. ')
else:
    print(f'Infelizmente, você não é elegível para realizar o empréstimo')
