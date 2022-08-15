linha = input().split()
a = int(linha[0])
b = int(linha[1])

if a == 1:
    a = 4.0
elif a == 2:
    a = 4.5
elif a == 3:
    a = 5.0
elif a == 4:
    a = 2.0
elif a == 5:
    a = 1.5

total = a*b

print(f"Total: R$ {total:.2f}")
