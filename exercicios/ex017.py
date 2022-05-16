from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
h = hypot(ca, co)
print(f'Hipotenusa = {h}')

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print(f'Hipotenusa = {(co**2 + ca**2)**0.5}')
