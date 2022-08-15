N = int(input())

lista = []

for i in range(N):

    c = int(input())

    if c % 2 == 0:
        if c > 0:
            lista.append("EVEN POSITIVE")
        if c < 0:
            lista.append("EVEN NEGATIVE")
    if c % 2 == 1:
        if c > 0:
            lista.append("ODD POSITIVE")
        if c < 0:
            lista.append("ODD NEGATIVE")
    if c == 0:
        lista.append("NULL")

for j in range(N):
    print(lista[j])


