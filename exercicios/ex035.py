c1, c2, c3 = input('Informe 3 comprimentos de retas: ').split()
c1 = float(c1)
c2 = float(c2)
c3 = float(c3)

if c2 % c3 < c1 < c2 + c3:
    if c1 % c3 < c2 < c1 + c3:
        if c1 % c2 < c3 < c1 + c2:
            print('Pode formar um triângulo!')
        else:
            print('Não pode formar um triângulo')
    else:
        print('Não pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
