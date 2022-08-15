n = int(input())
for c in range(n):
    linha = input().split()
    s1 = str(linha[0])
    s2 = str(linha[1])
    if len(s1) < len(s2):
        menor = s1
        maior = s2
    else:
        menor = s2
        maior = s1
    s3 = ''
    for i in range(len(menor)):
        s3 += s1[i]
        s3 += s2[i]
    for l in range(len(maior) - len(menor)):
        i+=1
        s3 += maior[i]
    print(s3)


