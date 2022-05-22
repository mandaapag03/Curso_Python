n1, n2, n3 = input('Informe 3 números: ').split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
maior = 0
menor = 1_000_000

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
