from random import sample, shuffle
n1, n2, n3, n4 = input('Informe os nomes dos alunos: ').split()
nomes = [n1, n2, n3, n4]
print(f'A ordem é {sample(nomes, 4)})')
#OU sample OU shuffle 
n1, n2, n3, n4 = input('Informe os nomes dos alunos: ').split()
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print(nomes)
