while (True):
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    if x == 0 or y == 0:
        break
    else:
        if x > 0 and y > 0:
            print("primeiro")
        if x > 0 and y < 0:
            print("quarto")
        if x < 0 and y < 0:
            print("terceiro")
        if x < 0 and y > 0:
            print("segundo")
