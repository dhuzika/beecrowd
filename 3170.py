b = int(input())
g = int(input())
f = g//2 - b

if g//2 <= b:
    print("Amelia tem todas bolinhas!")
if g//2 > b:
    print(f"Faltam {f} bolinha(s)")