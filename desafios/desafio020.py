#O professor quer determinar a ordem de apresentação de um trabalho, são quatro alunos.
from random import sample
n1, n2, n3, n4 = input('Informe os nomes dos alunos: ').split()
nomes = [n1, n2, n3, n4]
print(f'A ordem é {sample(nomes, 4)})')
