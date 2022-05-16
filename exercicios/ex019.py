from random import choice
n1, n2, n3, n4 = input('Informe o nome dos alunos: ').split()
nomes = [n1, n2, n3, n4]
print(f'O aluno escolhido é {choice(nomes)}')
