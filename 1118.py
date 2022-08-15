nota_valida = 0
soma_nota = 0
j=True
while j == True:
    nota = float(input())
    if nota < 0.00 or nota > 10.00:
        print("nota invalida")
    else:
        nota_valida += 1
        soma_nota += nota
        if nota_valida >= 2:
            print(f"media = {(soma_nota/nota_valida):.2f}")
            soma_nota = 0
            nota_valida = 0
            b = False
            while b == False:
                X = int(input("novo calculo (1-sim 2-nao)\n"))
                if X == 1:
                    b = True
                if X == 2:
                    j = False
                    break
