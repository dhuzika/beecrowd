import string
lista = []
s = int(input())
x = string.ascii_uppercase
d = dict.fromkeys(x)
li = list(d.keys())
for o in range(26):
    d.update({li[o]: o})
for c in range(s):
    soma = 0
    L = int(input())
    z = 0
    for n in range(L):
        S = list(input())
        for m in S:
            soma += d[m] + n + z
            z += 1
        z = 0
    print(soma)
