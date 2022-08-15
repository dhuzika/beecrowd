n = int(input())
for c in range(n):
    a = int(input())
    b = str(input()).split()
    c = str(input()).split()
    if int(b[2]) % 2 == 0:
        b[2] = a
    else:
        b[2] = 0
    if int(c[2]) % 2 == 0:
        c[2] = a
    else:
        c[2] = 0
    valor1 = (int(b[0]) + int(b[1]))/2 + int(b[2]) 
    valor2 = (int(c[0]) + int(c[1]))/2 + int(c[2]) 
    if valor1 > valor2:
        print("Dabriel")
    elif valor1 < valor2:
        print("Guarte")
    else:
        print("Empate")
