n = int(input())
for c in range(n):
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    i=0
    j=0
    s=0
    while i != y:
       if (x + j) % 2 == 1:
           i+=1
           s+=(x+j)
       j+=1
    print(s)

