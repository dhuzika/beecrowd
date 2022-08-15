n = int(input())
for c in range(n):
    lista = []
    k = ''
    s = str(input())
    s+='a'
    for i in s:
        if i.isnumeric():
            k += i
        else:
            try:
                lista.append(int(k))
                k = ''
            except:
                k = ''
    print(sum(lista))

