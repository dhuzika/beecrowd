linha = input().split()
a = int(linha[0])
b = int(linha[1])

lista = [a, b]

if b > a:
  tempo = b-a
else:
  tempo = (24-a) + b

print(f"O JOGO DUROU {tempo} HORA(S)")