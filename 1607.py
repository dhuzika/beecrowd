import string
n = int(input())
for m in range(n):
    letras = string.ascii_lowercase
    linha = input().split()
    a = str(linha[0])
    b = str(linha[1])
    lista = []
    lista2 = []
    for i in a:
        lista.append(letras.index(i))
    for j in b:
        lista2.append(letras.index(j))
    lista3 = []
    for c in range(len(lista)):
        if lista[c] - lista2[c] <= 0:
            lista3.append(abs(lista[c] - lista2[c]))
        elif lista2[c] < lista[c]:
            lista3.append(26 - lista[c] + lista2[c])
        elif lista[c] > lista2[c]:
            lista3.append(26 - lista[c] + lista2[c])

    print(sum(lista3))
