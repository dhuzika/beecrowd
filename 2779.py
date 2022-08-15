n = int(input())
m = int(input())
lista = []
for c in range(m):
    x = int(input())
    if x not in lista:
        lista.append(x)
print(n - len(lista))