#professor quer sortear 1 aluno dos 4
import random
a1, a2, a3, a4 = input('Informe o nome dos alunos: ').split()
escolha = random.randint(1, 4)
if escolha == 1:
    print(a1)
elif escolha == 2:
    print(a2)
elif escolha == 3:
    print(a3)
else:
    print(a4)
