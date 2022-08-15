cawcaw = 0
soma = 0
while cawcaw != 3:
    piscada = input()
    if piscada != 'caw caw':
        piscada = piscada.replace('-','0')
        piscada = piscada.replace('*','1')
        piscada = int(piscada, 2)
        soma += piscada
    else:
        print(soma)
        cawcaw += 1
        soma = 0