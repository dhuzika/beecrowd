nota_valida = 0
soma_nota = 0
while nota_valida != 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        nota_valida += 1
        soma_nota += nota
print(f"media = {soma_nota/2}")