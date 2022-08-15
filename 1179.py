i=0
lista_par = []
lista_impar = []
for c in range(15):
    n = int(input())
    if n % 2 == 0:
        lista_par.append(n)
    if n % 2 == 1:
        lista_impar.append(n)
    if len(lista_par) == 5:
        for v in range(len(lista_par)):
            print(f"par[{v}] = {lista_par[v]}")
        lista_par.clear()
    if len(lista_impar) == 5:
        for k in range(len(lista_impar)):
            print(f"impar[{k}] = {lista_impar[k]}")
        lista_impar.clear()

for h in range(len(lista_impar)):
    print(f"impar[{h}] = {lista_impar[h]}")

for u in range(len(lista_par)):
    print(f"par[{u}] = {lista_par[u]}")