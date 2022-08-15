n = int(input())
s=0
b=0
a=0
m=0
d=0
for c in range(n):
    linha = input().split()
    e = linha[0]
    g = linha[1]
    h = linha[2]
    if g == "bonecos":
        b+=int(h)
    if g == "arquitetos":
        a+=int(h)
    if g == "musicos":
        m+=int(h)
    if g == "desenhistas":
        d+=int(h)
s=b//8+a//4+m//6+d//12
print(s)
