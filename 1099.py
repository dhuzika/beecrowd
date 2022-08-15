n = int(input())
i = 0


for c in range(1, n+1):
    linha = input().split()
    z = 0
    a = int(linha[0])
    b = int(linha[1])


    if a > b:
        for i in range(b+1, a):
            if i % 2 == 1:
                z += i
    if a < b:
        for i in range(a+1, b):
            if i % 2 == 1:
                z += i

    if a == b:
        z += 0

    print(z)
