import math

linha1 = input().split()
x1 = float(linha1[0])
y1 = float(linha1[1])

linha2 = input().split()
x2 = float(linha2[0])
y2 = float(linha2[1])

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(f"{distancia:.4f}")
