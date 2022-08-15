coluna = int(input())
operacao = str(input())
soma = 0
i=0
x = False
y = False
while True:
    try:
        for c in range(144):
            a = float(input())
            if coluna + 12*i == c:
                soma+=a
                i+=1
        media = soma/12
        if operacao == "S":
            x=True
        if operacao == "M":
            y=True
        if x:
            print(f"{soma:.1f}")
        if y:
            print(f"{media:.1f}")
        break
    except EOFError:
        break