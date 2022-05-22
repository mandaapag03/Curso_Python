km = float(input('Distância da sua viagem: '))
preco = km * 0.50 if km <= 200 else km * 0.45
print(f'Valor da passagem: R$ {preco:.2f}')
