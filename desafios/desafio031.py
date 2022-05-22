km = float(input('Distância da sua viagem: '))
if km <= 200:
    print(f'Valor da passagem: R$ {km*0.50}')
else:
    print(f'Valor da passagem: R$ {km * 0.45}')
    
