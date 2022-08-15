n = int(input())
total_menino = 0
total_menina = 0
for c in range(n):
    for i in range(3):
        linha = input().split()
        x = int(linha[0])
        d = int(linha[1])
        total_menino = total_menino + x*d
    for b in range(3):
        linha = input().split()
        x = int(linha[0])
        d = int(linha[1])
        total_menina = total_menina + x*d
    if total_menino > total_menina:
        print("JOAO")
    if total_menina > total_menino:
        print("MARIA")
    total_menina = 0
    total_menino = 0

