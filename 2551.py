while True:
    try:
        n = int(input())
        maior = 0
        for c in range(1, n+1):
            linha = input().split()
            duracao = int(linha[0])
            distancia = int(linha[1])
            if distancia/duracao > maior:
                print(c)
                maior = distancia/duracao
    except:
        break