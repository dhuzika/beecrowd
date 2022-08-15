n = int(input())
ss=0
sb=0
sa=0
ss1=0
sb1=0
sa1=0
for c in range(n):
    nome = str(input())
    linha = input().split()
    s = int(linha[0])
    b = int(linha[1])
    a = int(linha[2])
    ss+=s
    sb+=b
    sa+=a
    linha1 = input().split()
    s1 = int(linha1[0])
    b1 = int(linha1[1])
    a1 = int(linha1[2])
    ss1+=s1
    sb1+=b1
    sa1+=a1
ps = ss1/ss*100
pb = sb1/sb*100
pa = sa1/sa*100
print(f"Pontos de Saque: {ps:.2f} %.")
print(f"Pontos de Bloqueio: {pb:.2f} %.")
print(f"Pontos de Ataque: {pa:.2f} %.")
