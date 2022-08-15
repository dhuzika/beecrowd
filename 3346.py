linha = input().split()
f1 = float(linha[0])
f2 = float(linha[1])
inicial = 100
d1 = inicial * f1/100 + inicial
d2 = d1 * f2/100 + d1
final = d2
print(f"{final-inicial:.6f}")