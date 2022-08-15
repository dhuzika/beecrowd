while True:
    try:
        s = str(input()).lower().split()
        k=0
        l=''
        lista = []
        for i in s:
            for j in i:
                lista.append(j)
                break
        lista2 = lista.copy()
        for c in range(len(lista)):
            try:
                if lista[c] == lista2[c+1] and l != lista[c]:
                    k+=1
                    l = lista[c]
                else:
                    l = lista[c]
            except:
                continue
        print(k)
    except:
        break