import string
n = int(input())
lista = []
u = False
vogais = ["a","e","i","o","u"]

for c in range(n):
    p = str(input()).lower()
    for i in range(len(p)):
        lista.append(p[i])
    for k in range(len(lista)):
        try:
            if lista[k] not in vogais and lista[k+1] not in vogais and lista[k+2] not in vogais:
                u = True
        except:
            continue

    lista = []
    if u:
        print(f"{p.capitalize()} nao eh facil")
    else:
        print(f"{p.capitalize()} eh facil")
    u=False