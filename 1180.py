n = int(input())
lista = []
posicao = 0

linha = input().split()
for u in range(n):
    a = int(linha[u])
    lista.append(a)
print(f"Menor valor: {min(lista)}")
for v in range(len(lista)):
    if lista[v] == min(lista):
        posicao=v
print(f"Posicao: {posicao}")