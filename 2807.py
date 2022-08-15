n = int(input())
n1 = 1
n2 = 1
n3=0
lista = [1, 1]



for c in range(n-2):
    n3 = n1 + n2
    lista.append(n3)
    n1=n2
    n2=n3



lista_reversa = lista[::-1]

if n == 1:
    print(1)
if n == 2:
    print("1 1")
elif n > 2:
    print(str(lista_reversa).replace("[","").replace("]","").replace(",",""))