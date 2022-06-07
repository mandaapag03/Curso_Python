def cria_matriz(l,c):
        m = []
        linha = c * [0]
        for i in range(l):
                m.append(linha[:])
        return m

def exibe_matriz(matriz):
        for linha in matriz:
                print('|', *linha, '|')
def preenche_matriz(m,l,c):
        for i in range(l):
                for j in range(c):
                        m[i][j] = float(input(f'M[{i}][{j}] = '))
                print()
#alunos = [[5.5,7.0,8.7],[8.0, 6.0, 9.2],[7.8, 8.3, 8.5],[0.0, 9.9, 9.1]]
alunos = cria_matriz(4,3)
preenche_matriz(alunos,4,3)
exibe_matriz(alunos)
