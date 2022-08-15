N = int(input())

lista = []

for c in range(N):
    a = int(input())
    lista.append(a)

contador = 0

for numero in lista:
    if 10 <= numero <= 20:
        contador += 1

print(f"{contador} in\n{len(lista)-contador} out")
