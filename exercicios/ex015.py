d = int(input('Quantidade de dias de aluguel do carro: '))
km = float(input('Quantos KM rodados: '))
print(f'Valor a pagar: R$ {(d * 60) + (km * 0.15):.2f}')
