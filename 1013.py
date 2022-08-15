linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
maior_ab = (a+b+abs(a-b))/2
maior = (maior_ab+c+abs(maior_ab-c))/2
print(f"{maior:.0f} eh o maior")
