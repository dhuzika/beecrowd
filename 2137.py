while True:
    try:
        n = int(input())
        lista = []
        for c in range(n):
            s = str(input())
            lista.append(s)
        lista = sorted(lista)
        for i in lista:
            print(i)
    except:
        break