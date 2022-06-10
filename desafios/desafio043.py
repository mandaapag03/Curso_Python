peso = float(input('Informe seu peso(kg): '))
altura = float(input('Informe sua altura(m): '))
imc = peso/altura**2
if imc > 40:
    print(f'IMC {imc:.2f}: Obesidade Mórbida')
else:
    if imc < 18.5:
        print(f'IMC {imc:.2f}: Abaixo do Peso')
    elif 18.5 <= imc < 25:
        print(f'IMC {imc:.2f}: Peso ideal')
    elif 25 <= imc < 30.0:
        print(f'IMC {imc:.2f}: Sobrepeso')
    else:
        print(f'IMC {imc:.2f}: Obesidade')
