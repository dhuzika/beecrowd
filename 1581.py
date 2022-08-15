n = int(input())
for c in range(n):
    n2 = int(input())
    lista = []
    for j in range(n2):
        s = str(input())
        lista.append(s)
    if len(set(lista)) == 1:
        print(lista[0])
    else:
        print("ingles")
