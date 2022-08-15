n = int(input())
meninas = 0
meninos = 0
for c in range(n):
    nomeg=str(input()).split()
    if nomeg[1] == "M":
        meninos +=1
    if nomeg[1] == "F":
        meninas += 1
print(f"{meninos} carrinhos")
print(f"{meninas} bonecas")

