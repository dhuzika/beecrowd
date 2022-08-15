N = int(input())
for c in range(N):
    linha = input().split()
    a=float(linha[0])
    b=float(linha[1])
    c=float(linha[2])
    media = (a*2 + b*3 + c*5)/10
    print(f"{media:.1f}")