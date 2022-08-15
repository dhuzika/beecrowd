linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

valores = [a,b,c]
crescente = sorted(valores)
decrescente = crescente[::-1]
a = decrescente[0]
b = decrescente[1]
c = decrescente[2]

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == (b ** 2 + c ** 2):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > (b ** 2 + c ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < (b ** 2 + c ** 2):
        print('TRIANGULO ACUTANGULO')
    if (a == b == c):
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')
  
  
