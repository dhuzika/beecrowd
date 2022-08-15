linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

if A >= B + C or B >= A + C or C >= B + A:
    area = ((A+B)*C)/2
    print(f"Area = {area:.1f}")

else:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
