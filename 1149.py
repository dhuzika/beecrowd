lista = []
i=0
soma = 0
linha = input().split()
a = int(linha[0])
z = int(linha[-1])

while i <= z-1:
    soma += a + i
    i+=1

print(soma)