n = int(input())
for c in range(n):
    i = 1
    lista = []
    a = int(input())
    while i != a:
        if a % i == 0:
            lista.append(i)
        i+=1
    if sum(lista) == a:
        print(f"{a} eh perfeito")
    else:
        print(f"{a} nao eh perfeito")