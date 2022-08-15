s = str(input())
lista = []
for c in range(len(s)):
    lista.append(s[c])
for i in range(len(lista)):
    try:
        if lista[i] + lista[i+1] == lista[i+2] + lista[i+3]:
            lista.pop(i)
            lista.pop(i)
    except:
        continue
resposta = ""

for elemento in lista:
    resposta+=elemento

print(resposta)



