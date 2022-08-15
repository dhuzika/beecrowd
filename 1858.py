n = int(input())
lista = list(map(int,input().split()))
menor = min(lista)
print(lista.index(menor) + 1)
