while True:

    p = 0
    o=0
    b=-1
    lista = []
    lista_ultima = []
    a= " "
    n = int(input())
    if n == 0:
        break

        continue
    for c in range(100):
        lista.append(2**p)
        p+=1

    for y in range(n):
        lista_ultima.append(lista[n+b])
        b+=1
    tamanho_ultimo = len(str(lista_ultima[-1]))

    for k in range(n):
        for c in range(n):
            if len(str(lista[c + o])) == tamanho_ultimo - 14:
                if c != 0:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])) + 1)}{lista[c + o]}", end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-13:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-12:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-11:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-10:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-9:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-8:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-7:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-6:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-5:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-4:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-3:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-2:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a * (tamanho_ultimo - len(str(lista[c + o])))}{lista[c + o]}", end='')
            if len(str(lista[c+o])) == tamanho_ultimo-1:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o])))}{lista[c+o]}",end='')
            if len(str(lista[c+o])) == tamanho_ultimo:
                if c != 0:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o]))+1)}{lista[c+o]}",end='')
                else:
                    print(f"{a*(tamanho_ultimo-len(str(lista[c+o])))}{lista[c+o]}",end='')
        print()
        o+=1
    print()

