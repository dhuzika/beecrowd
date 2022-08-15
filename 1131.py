c=0
inter = 0
gremio=0
empate =0
j = True
while j == True:
    linha = input().split()
    a = int(linha[0])
    b = int(linha[1])
    c += 1
    if a > b:
        inter +=1
    if a < b:
        gremio +=1
    if a == b:
        empate +=1

    p = int(input("Novo grenal (1-sim 2-nao)\n"))
    if p == 2:
        j=False
        break

print(f"{c} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
if gremio > inter:
    print("Gremio venceu mais")
if inter > gremio:
    print("Inter venceu mais")
if inter == gremio:
    print("Nao houve vencedor")