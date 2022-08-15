n = int(input())
lista = []
listal = []
listaj = []
listac= []
listar = []
listas = []

coelho = 0
for c in range(n):
    a = str(input())

    if len(a) == 4:
        lista.append(int(a[0:2]))

    if len(a) == 3:
        lista.append(int(a[0]))

    if "C" in a:
        listal.append("C")

    if "R" in a:
        listal.append("R")

    if "S" in a:
        listal.append("S")


for i in range(len(lista)):
    listaj.append(lista[i] * listal[i])
    if "C" in listaj[i]:
        listac.append(lista[i])
    if "R" in listaj[i]:
        listar.append(lista[i])
    if "S" in listaj[i]:
        listas.append(lista[i])

totalC = sum(lista)
totalc = sum(listac)
totalr = sum(listar)
totals = sum(listas)

print(f"Total: {sum(lista)} cobaias")
print(f"Total de coelhos: {sum(listac)}")
print(f"Total de ratos: {sum(listar)}")
print(f"Total de sapos: {sum(listas)}")
print(f"Percentual de coelhos: {((totalc * 100)/totalC):.2f} %")
print(f"Percentual de ratos: {((totalr * 100)/totalC):.2f} %")
print(f"Percentual de sapos: {((totals * 100)/totalC):.2f} %")