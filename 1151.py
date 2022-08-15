j = True
lista = [0, 1]
while j == True:
    # 0 1 1 2 3
    n= int(input())
    n1 = 0
    n2 = 1
    if n == 0:
        break
    if n == 1:
        print(f"0")
        break
    if n == 2:
        print(f"0 1")
        break

    for c in range(n-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        lista.append(n3)
    z = str(lista)
    m = z.replace(",", "")
    b = m.replace("[", "")
    x = b.replace("]", "")
    print(x)
    break