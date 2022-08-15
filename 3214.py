linha = input().split()

E = int(linha[0])
F = int(linha[1])
C = int(linha[2])
c = 0
z = E + F
while z >= C:
    z -= C
    z += 1
    c+=1

print(c)

