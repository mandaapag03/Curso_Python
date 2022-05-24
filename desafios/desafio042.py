a, b, c = input('Digite 3 comprimentos de reta: ').split()
a = float(a)
b = float(b)
c = float(c)

if a > b + c or b > a + c or c > a + b:
    print('Os segmentos de reta NÃO PODEM formar o triângulo')
else:
    if a == b == c:
        print('Os segmentos PODEM formar um triângulo EQUILÁTERO')
    elif a == b or b == c or a == c:
        print('Os segmentos PODEM formar um triângulo ISÓSCELES')
    else:
        print('Os segmentos PODEM formar um triângulo ESCALENO')

        
