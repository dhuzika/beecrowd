linha = input().split()
h = int(linha[0])
z = int(linha[1])
l = int(linha[2])
if h > z and h < l:
    print("huguinho")
if h > l and h < z:
    print("huguinho")
if l > h and l < z:
    print("luisinho")
if l > z and l < h:
    print("luisinho")
if z > h and z < l:
    print("zezinho")
if z > l and z < h:
    print("zezinho")