lista = []
for c in range(0,20):
    a = int(input())
    lista.append(a)
lista = lista[::-1]
for i in range(len(lista)):
    print(f"N[{i}] = {lista[i]}")
