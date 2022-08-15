while True:    
    try:
        n = int(input())
        linha = input().split()
        lista = []
        for c in range(n):
            a = int(linha[c])
            lista.append(a)
        if max(lista) < 10:
            print(1)
        if 10 <= max(lista) < 20:
            print(2)
        if max(lista) >= 20:
            print(3)
    except EOFError:
        break
