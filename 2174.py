n = int(input())
lista = []
for c in range(n):
    s = str(input())
    lista.append(s)
lista = set(lista)
print(f"Falta(m) {151-len(lista)} pomekon(s).")