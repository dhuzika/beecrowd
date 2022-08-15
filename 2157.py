n = int(input())
for c in range(n):
    linha = input().split()
    n1 = int(linha[0])
    n2 = int(linha[1])
    lista = [n1]
    while n2 not in lista:
        lista.append(n1+1)
        n1+=1
    lista = str(lista).replace("[","").replace("]","").replace(",","").replace(" ","")
    lista+=lista[::-1]
    print(lista)