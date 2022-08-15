n = int(input())
linha = input().split()
total = 0
lista = [0]
lista2 = []
while total < len(linha):
    lista.append(int(linha[total]))
    total += 1
for c in range(1, n+1):
    if lista[c] < lista[c-1]:
        lista2.append(c)
try:
    print(lista2[0])
except IndexError:
    print(0)
