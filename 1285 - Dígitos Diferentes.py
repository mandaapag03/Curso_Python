def separa(n):
    n = str(n)
    n = list(n)
    l = []
    for _ in len(n):
        n = int(n)
        num = n % 10
        l.append(num)
        n = n // 10
    l.reverse()
    return l
        
x, y = input().split()
x, y = int(x), int(y)
sem_digitos = 0
for n in range(x, y + 1):
    n = separa(n)
    for item in n:
        valor = n.count(item)
        if valor == 1:
            sem_digitos += 1
print(sem_digitos)
