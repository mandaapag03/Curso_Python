valor = float(input())
#print(f'Centímetros: {valor * 100} cm e milímetros é {valor * 1000} mm')
km = valor/1000
hm = valor/100
dam = valor/10
dm = valor*10
cm = valor*100
mm = valor*1000
print(f'{km} km\n{hm} hm\n{dam} dam\n{dm} dm\n{cm} cm\n{mm} mm')
