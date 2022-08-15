n = int(input())
for c in range(n):
    linha = input().split()
    a = str(linha[0])
    b = str(linha[1])
    z = 0
    u = False
    for c in range(len(b)):
        try:
            if a[-(c + 1)] == b[-(c + 1)]:
                z += 1
        except:
            u = True
            print("nao encaixa")
            break
    if z == len(b):
        print("encaixa")
    else:
        if not u:
            print("nao encaixa")
