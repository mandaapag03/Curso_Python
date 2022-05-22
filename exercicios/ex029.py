vel = float(input('Velocidade do carro: '))
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80)*7
    print(f'Sua multa é de R$ {multa:.2f}')
else:
    print('No limite de velocidade! Continue assim!')
    
