while True:
    linha = input().split()
    n1 = int(linha[0])
    n2 = int(linha[1])
    s = str(n1+n2)
    if s == "0":
        break
    r = s.replace("0","")
    print(r)
