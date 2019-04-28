init = 56
max = 5
last_num = max + 2
lista_ganar = []
while last_num < init:
    lista_ganar.append(last_num)
    last_num += max+1

arbol = {}
for i in range(1,init+1):
    arbol[i] = [i-a for a in range(1,max+1) if i-a >= 0]

arbol_valores = {}
for a in arbol:
    for b in arbol[a]:
        arbol_valores[(a,b)] = 1 if b in lista_ganar else 0