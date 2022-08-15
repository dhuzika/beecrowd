linha = input().split()
n = int(linha[0])
m = int(linha[1])
lista = []
lista_reversa = []
bagunca = ""
lista2 = []
lista_reversa2 = []
lista_resposta = []
lista_nao = []

for c in range(n):
    fruta = str(input()).lower()
    lista.append(fruta)
    lista2.append(fruta)
    lista_reversa.append(fruta[::-1])
    lista_reversa2.append(fruta[::-1])

for i in range(m):
    bagunca += str(input()).lower()

for j in range(n):
    if lista[j] in bagunca or lista_reversa[j] in bagunca:
        lista[j] = True
    else:
        lista[j] = False

for b in range(len(lista)):
    if lista[b] == True:
        print(f"Sheldon come a fruta {lista2[b]}")
    if lista[b] == False:
        print(f"Sheldon detesta a fruta {lista2[b]}")



