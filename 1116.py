n = int(input())
for c in range(n):
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    if y == 0:
        print("divisao impossivel")
    else:
        print(x/y)