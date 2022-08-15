import math
linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

delta = B**2 - 4 * A * C
if delta < 0.0 or A == 0.0:
    print("Impossivel calcular")
else:
    x1 = (- B + (B ** 2 - 4 * A * C) ** (1 / 2)) / (2 * A)
    x2 = (- B - (B ** 2 - 4 * A * C) ** (1 / 2)) / (2 * A)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")


